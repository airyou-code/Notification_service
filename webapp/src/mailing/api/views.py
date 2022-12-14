import datetime
from rest_framework.viewsets import  ModelViewSet, ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from django_celery_beat.models import ClockedSchedule, PeriodicTask

from mailing.tasks import send_messages
from ..models import Client, Mailing, Message
from .serializers import ClientSerializer, MailingSerializer, MessageSerializer


class MessageAPIList(ReadOnlyModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filterset_fields = ['client', 'mailing']

class ClientAPIView(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tag', 'operator']

class MailingAPIView(ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        mailing = Mailing.objects.last()
        try:
            ctag = mailing.clients["tag"]
        except:
            ctag = None
        
        try:
            coperator = mailing.clients["operator"]
        except:
            coperator = None
        
        if ctag and coperator:
            clients = Client.objects.filter(tag=ctag, operator=coperator)
        elif ctag:
            clients = Client.objects.filter(tag=ctag)
        elif coperator:
            clients = Client.objects.filter(operator=coperator)
        else:
            clients = Client.objects.all()

        if not clients:
            mailing.delete()
            return Response(
                {
                    "message": "No client matches the filter, mailing has not been created",
                },status=status.HTTP_400_BAD_REQUEST,)

        now_time = datetime.datetime.now(mailing.start_time.tzinfo)
        count = len(clients)

        if mailing.start_time <= now_time:
            if mailing.end_time >= now_time:
                send_messages.delay(mailing.id)
                return Response(
                    {
                        "message": f"Mailing ({count} cliemts) has been successfully registered!",
                        "clients": count
                    },status=status.HTTP_201_CREATED)
            else:
                mailing.delete()
                return Response(
                    {
                        "message": "The end time is less than the current time",
                    },status=status.HTTP_400_BAD_REQUEST,)

        else:
            schedule, created = ClockedSchedule.objects.get_or_create(clocked_time=mailing.start_time)
            task = PeriodicTask.objects.create(
                one_off=True,  
                clocked=schedule,
                name=f"Mailing {mailing.id} waiting for up to {schedule.clocked_time}",
                task="mailing.tasks.send_messages",
                args=[mailing.id],
            )

            return Response(
                {
                    "message": f"Mailing ({count} cliemts) has been successfully registered and is waiting!",
                    "start": f"{schedule.clocked_time}",
                    "clients": count
                },status=status.HTTP_201_CREATED,)
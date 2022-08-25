from ast import operator
import datetime
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from celery.result import AsyncResult
from django_celery_beat.models import ClockedSchedule, PeriodicTask

from ..models import Client, Mailing, Message
from .serializers import ClientSerializer, MailingSerializer


class ClientAPIList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

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
            return Response({"message": "Ни один клиент не соответствует фильтру,рассылка не была создана",},
                            status=status.HTTP_400_BAD_REQUEST,
                            )

        now_time = datetime.datetime.now(mailing.start_time.tzinfo)
        # for client in clients:
        #     pass
            # Message.objects.create(client=client, mailing=mailing)

        count = len(clients)
        schedule, created = ClockedSchedule.objects.get_or_create(
            clocked_time=mailing.start_time
        )

        scheduled_task = PeriodicTask.objects.create(
                        clocked=schedule,
                        name="Рассылка {} в ожидaнии до {}".format(
                            mailing.id, schedule.clocked_time
                        ),
                        task="mailing.tasks.send_messages",
                        args=[mailing.id],
                        one_off=True,  
        )
        # scheduled_task = PeriodicTask.objects.create(
        #                 clocked=schedule,
        #                 name="Рассылка {} в ожидонии до {}".format(
        #                     mailing.id, schedule.clocked_time
        #                 ),
        #                 task="message_service.mailing.tasks.send_messages_now_task",
        #                 args=JsonResponse([mailing.id], safe=False),
        #                 one_off=True,
        #             )
        # status=status.HTTP_201_CREATED,
        if mailing.start_time <= now_time:

            print(                        {
                            "message": "Рассылка успешно зарегистрирована!",
                            "count_message": count,
                        },)

        return Response(
                    {
                        "message": "Рассылка успешно зарегистрирована и находится в ожидании!",
                    },
                    status=status.HTTP_201_CREATED,
                )
        # else:
        #     mailing.delete()
        #     return Response({"message": "Ни один клиент не соответствует фильтру,рассылка не была создана",},
        #                     status=status.HTTP_400_BAD_REQUEST,
        #                     )



# class ClientAPIDetailView(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):

#     serializer_class = ClientSerializer

#     def get_queryset(self):
#         pk = self.kwargs.get("pk")
#         if not pk:
#             return Client.objects.all()

#         return Client.objects.filter(pk=pk)

    # @action(methods=['get'], detail=True)
    # def category(self, request, pk=None):
    #     cats = Category.objects.get(pk=pk)
    #     return Response({'cats': cats.name})



# class ClientAPIView(APIView):

#     def get(self, request):
#         clients = Client.objects.all()
#         # serializer_class = ClientSerializer
#         return Response({'clients': ClientSerializer(clients, many=True).data})
    
#     def post(self, request):
#         serializer = ClientSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({"message": "Client added"},status=status.HTTP_201_CREATED,)
    
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)

#         if not pk:
#             return Response({"error": "Method PUT not allowed"}, status=status.HTTP_400_BAD_REQUEST,)
        
#         try:
#             instance = Client.objects.get(pk=pk)
#         except:
#             return Response({"error": "Method PUT not allowed"}, status=status.HTTP_404_NOT_FOUND,)
        
#         serializer = ClientSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"message": "Client added"},status=status.HTTP_201_CREATED,)
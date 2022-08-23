from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Client, Mailing, Message
from .serializers import ClientSerializer

class ClientAPIList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientAPIView(APIView):

    def get(self, request):
        clients = Client.objects.all()
        # serializer_class = ClientSerializer
        return Response({'clients': ClientSerializer(clients, many=True).data})
    
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Client added"},status=status.HTTP_201_CREATED,)
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response({"error": "Method PUT not allowed"}, status=status.HTTP_400_BAD_REQUEST,)
        
        try:
            instance = Client.objects.get(pk=pk)
        except:
            return Response({"error": "Method PUT not allowed"}, status=status.HTTP_404_NOT_FOUND,)
        
        serializer = ClientSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Client added"},status=status.HTTP_201_CREATED,)
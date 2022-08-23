from django.shortcuts import render
from rest_framework import generics
from .api.serializers import ClientSerializer
from .models import Client, Mailing, Message


class ClientAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pass
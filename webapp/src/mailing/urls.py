from django.contrib import admin
from django.urls import path, include
from .api.views import ClientAPIList, ClientAPIView, MailingAPIView
from . import views

from rest_framework import routers

router1 = routers.DefaultRouter()
router2 = routers.DefaultRouter()
router1.register(r'client', ClientAPIView, basename='client')
router2.register(r'mailing', MailingAPIView, basename='mailing')

# print(router1.urls)

urlpatterns = [
    # path('v1/', ClientAPIDetailView.as_view()),
    # path('', include(router1.urls, router2.urls ))
] + router2.urls + router1.urls
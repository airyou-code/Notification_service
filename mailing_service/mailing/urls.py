from django.contrib import admin
from django.urls import path
from .api.views import ClientAPIView, ClientAPIList, ClientAPIDetailView
from . import views

urlpatterns = [
    path('v1/<int:pk>', ClientAPIDetailView.as_view())
]
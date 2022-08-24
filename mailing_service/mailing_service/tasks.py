import requests as r
import uuid
from celery import shared_task
from django.conf import settings

@shared_task
def download_a_cat(asd):
    print(f"============URRRRRRRRRRRAAAAAAAA========{asd}")
    return True
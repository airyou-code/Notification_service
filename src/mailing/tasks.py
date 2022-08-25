from celery import Celery
from mailing_service.celery import app
from celery import shared_task
from .models import Client, Mailing, Message
from django.shortcuts import get_object_or_404

import requests
import time
import datetime
import json


@app.task
def add(x, y):
    print(f'{x} + {y} = {x+y}')
    return True

@shared_task
def send_messages(mailing_id):
    mailing = Mailing.objects.get(pk=mailing_id)
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

    for client in clients:
        pass
        message = Message.objects.create(client=client, mailing=mailing)
        # message = ( mailing=mailing, client=client)
        auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTI3ODIwMDUsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6ImFpcnlvdVRfVCJ9.OcVRI8FK-Fs2mcFgMY-XNjodR_j5QI25huYgty50U5I"
        headers = {
            "Authorization": f"Bearer {auth_token}",
            "Content-Type": "application/json",
        }
        data = json.dumps({
                "id": int(message.id),
                "phone": int(client.phone_number[1:]),
                "text": f"{mailing.text}",
                })

        url = f"https://probe.fbrq.cloud/v1/send/{message.id}"
        r = requests.post(url=url, headers=headers, data=data)
        # print()
        print(f"{message.id}:r  +7{int(client.phone_number[1:])}, {r}, ")
        time.sleep(2)
        message.sending_status = True
        message.save()

    # mailing.end_time = datetime.datetime.now(mailing.start_time.tzinfo)
    # mailing.save()
    # Client.objects.create(phone_number="79156850667", operator="915", tag="YRA")
    print(f"yes:{mailing_id}")
    

@app.task
def ad():
    print('sdksdfdfsd')
    return True

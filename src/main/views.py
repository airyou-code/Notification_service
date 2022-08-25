import os
from django.shortcuts import render
import requests
from mailing.models import Client
# Create your views here.
def index(request):
    url = 'http://127.0.0.1:8000/api/client/'
    tag = 'a1'
    params = {
            'tag' : tag
        }
    requests = request
    index = requests.get(url=url, params=params).json()
    # os.environ.get('HOSTNAME')
    clients = Client.objects.get(
                pk=2
            )
    clients.tag = "[][][][][]"
    clients.save()
    
    print(clients)
    return render(request, 'main/index.html', {"a":index})

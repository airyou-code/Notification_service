from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    url = 'http://127.0.0.1:8000/api/v1/'
    index = requests.get(url=url).json()
    print(index)
    return render(request, 'main/index.html', {"a":index[0]['phone_number']})
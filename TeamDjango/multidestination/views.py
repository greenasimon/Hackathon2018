import requests
# Create your views here.
import http.client
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'home.html')


def results(request,dest):
    api = findBookingAPI(request.path.split('/')[2])
    qryParams = {"language":"en_US","text":"\"+dest+\""}


    headers = {
        'authorization': "Basic d29tZW5pbnRlY2gyMDE4OjJEY2RDWm5UZmo=",
        'cache-control': "no-cache",
        'postman-token': "25ba4d68-b138-6a20-605d-c44b22c976a5"
    }

    response = requests.request("GET", api, headers=headers, params=qryParams)

    #return HttpResponse(response)
    return HttpResponse(response.json()["result"][0]['id'])

def findBookingAPI(path):
    APIDict = {
        'search':"https://distribution-xml.booking.com/2.2/json/autocomplete"
    }
    return APIDict[path]

def getResponse(url):
    response = requests.get(url)
    return response


from django.shortcuts import render, redirect
import requests
# Create your views here.
from django.http import HttpResponse
from multidestination.forms import TripHotelSearchForm

url = "https://distribution-xml.booking.com/2.0/json/countries"

headers = {
    'Authorization': "Basic d29tZW5pbnRlY2gyMDE4OjJEY2RDWm5UZmo=",
    'cache-control': "no-cache",
    'Postman-Token': "8239643c-8d84-4d54-b34f-c5ff77d37750"
    }

def index(request):
    return render(request,'home.html')

def home(request):
    print ("here")
    print (request.method)
    if(request.method=='POST'):
        form = TripHotelSearchForm(request.POST)
        #response = requests.request("GET", url, headers=headers)
        print ('here 2')
        #print (form.cleaned_data['city'])
        print (form.errors)
        if(form.is_valid()):
            print ('here 3')
            hotelform = form.save(commit=False)
            hotelform.save()
            return render(request,'tripRoad.html')
    else :
        form = TripHotelSearchForm()
    
    args = {'form' : form }
    return render(request, 'home.html',args)

def trip(request):
    return render(request, 'tripRoad.html')
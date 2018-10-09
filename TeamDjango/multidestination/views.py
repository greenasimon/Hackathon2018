from django.shortcuts import render
import requests
# Create your views here.
from django.http import HttpResponse
from multidestination.forms import HotelSearchForm

url = "https://distribution-xml.booking.com/2.0/json/countries"

headers = {
    'Authorization': "Basic d29tZW5pbnRlY2gyMDE4OjJEY2RDWm5UZmo=",
    'cache-control': "no-cache",
    'Postman-Token': "8239643c-8d84-4d54-b34f-c5ff77d37750"
    }

def index(request):
    return render(request,'home.html')

def home(request): 
   # print form.text
    if(request.method=='POST'):
        # send the data 
        form = HotelSearchForm(request.POST)
        print ("we are here")
        response = requests.request("GET", url, headers=headers)
    #    print(response.text)
        if(form.is_valid()):
            print ("we are here 2")
            hotelform = form.save(commit=False)
            hotelform.save()
            return redirect('home.html')
    else :
        form = HotelSearchForm()
    
    args = {'form' : form }
    return render(request, 'home.html',args)
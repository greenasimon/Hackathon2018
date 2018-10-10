from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse
from django.shortcuts import render
from multidestination.forms import TripHotelSearchForm
from django.http import JsonResponse
url = "https://distribution-xml.booking.com/2.0/json/countries"

headers = {
    'Authorization': "Basic d29tZW5pbnRlY2gyMDE4OjJEY2RDWm5UZmo=",
    'cache-control': "no-cache",
    'Postman-Token': "8239643c-8d84-4d54-b34f-c5ff77d37750"
}


def index(request):
    return render(request, 'home.html')


def home(request):
    print("here")
    print(request.method)
    if (request.method == 'POST'):
        form = TripHotelSearchForm(request.POST)
        # response = requests.request("GET", url, headers=headers)
        print(form.errors)
        if (form.is_valid()):
            hotelform = form.save(commit=False)
            hotelform.save()
            # print (request.POST)

            city1 = request.POST['city_1']
            checkin_date1 = request.POST['checkin_1']
            checout_date1 = request.POST['checkout_1']
            print(checout_date1)
            nub_pers1 = request.POST['numberOfPersons_1']

            city2 = request.POST['city_2']
            checkin_date2 = request.POST['checkin_2']
            checout_date2 = request.POST['checkout_2']
            nub_pers2 = request.POST['numberOfPersons_2']

            city3 = request.POST['city_3']
            checkin_date3 = request.POST['checkin_3']
            checout_date3 = request.POST['checkout_3']
            nub_pers3 = request.POST['numberOfPersons_3']

            #getcity details
            cityId1 = getCityID(city1)
            hoteldetails1 = getHotelAvailability(cityId1,checkin_date1,checout_date1)

            cityId2 = getCityID(city2)
            hoteldetails2 = getHotelAvailability(cityId2, checkin_date2, checout_date2)

            cityId3 = getCityID(city3)
            print(cityId3)
            hoteldetails3 = getHotelAvailability(cityId3, checkin_date3, checout_date3)

            budget = request.POST['budget']
            print(city1, city2, city3)
            #return JsonResponse(hoteldetails3)
            args = {'c1':city1,'c2':city2,'c3':city3,
                'checkin_date1': checkin_date1,'checkin_date2': checkin_date2,'checkin_date3': checkin_date3,
                'checout_date1': checout_date1, 'checout_date2': checout_date2, 'checout_date3': checout_date3, 
             'h1': hoteldetails1.json(),'h2': HttpResponse(hoteldetails2),'h3': HttpResponse(hoteldetails3) }
            #{'tripId' :tripId}
            return render(request,'tripRoad.html', args)
            #return HttpResponse(hoteldetails3)
            #return render(request, 'tripRoad.html')
    else:
        form = TripHotelSearchForm()

    args = {'form': form}
    return render(request, 'home.html', args)


def trip(request):
    return render(request, 'tripRoad.html')


def getCityID(dest):
    api = findBookingAPI("searchCity")
    res = results(api,dest)
    for item in res:
        if item['type'] == 'city':
            return item[id]
    return res[-1]['city_ufi']

    return results(api,dest)


def getHotelAvailability(cityid, checkin, checkout):
    api = findBookingAPI("HotelAvailability")
    qryParams = {"checkin":checkin,"checkout":checkout, "city_ids":cityid, "room1":'A,A', "extras":""}
    headers = {
        'authorization': "Basic d29tZW5pbnRlY2gyMDE4OjJEY2RDWm5UZmo=",
        'cache-control': "no-cache",
        'postman-token': "25ba4d68-b138-6a20-605d-c44b22c976a5"
    }
    response = requests.request("GET", api, headers=headers, params=qryParams)
    return response


def results(api,dest):
    #api = findBookingAPI(request.path.split('/')[2])
    qryParams = {"language":"en_US","text":"\"+dest+\""}


    headers = {
        'authorization': "Basic d29tZW5pbnRlY2gyMDE4OjJEY2RDWm5UZmo=",
        'cache-control': "no-cache",
        'postman-token': "25ba4d68-b138-6a20-605d-c44b22c976a5"
    }

    response = requests.request("GET", api, headers=headers, params=qryParams)

    #return HttpResponse(response)
    return response.json()["result"]
def findBookingAPI(path):
    APIDict = {
        'searchCity':"https://distribution-xml.booking.com/2.2/json/autocomplete",
        'HotelAvailability':"https://distribution-xml.booking.com/2.2/json/hotelAvailability"
    }
    return APIDict[path]

def getResponse(url):
    response = requests.get(url)
    return response
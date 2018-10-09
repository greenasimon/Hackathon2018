from django.db import models
from django.utils import timezone

# Create your models here.

class TripHotelSearch(models.Model):
    trip = models.AutoField(primary_key=True)
    city_1 = models.CharField(max_length = 100, blank=True)
    checkin_1 = models.DateField()
    checkout_1 = models.DateField()
    numberOfPersons_1 = models.CharField(max_length = 140)
    city_2 = models.CharField(max_length = 100, blank=True)
    checkin_2 = models.DateField()
    checkout_2 = models.DateField()
    numberOfPersons_2 = models.CharField(max_length = 140)
    city_3 = models.CharField(max_length = 100, blank=True)
    checkin_3 = models.DateField()
    checkout_3 = models.DateField()
    numberOfPersons_3 = models.CharField(max_length = 140)

    budget = models.IntegerField()

    def __str__(self):
        return str(self.city)

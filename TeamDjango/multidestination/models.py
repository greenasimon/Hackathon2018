from django.db import models
from django.utils import timezone

# Create your models here.

class TripHotelSearch(models.Model):
    # trip Id 
    city = models.CharField(max_length = 100, blank=True)
    checkin = models.DateField()
    checkout = models.DateField()
    numberOfPersons = models.CharField(max_length = 140)
    budget = models.IntegerField()

    def __str__(self):
        return str(self.city)

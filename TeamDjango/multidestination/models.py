from django.db import models
from django.utils import timezone

# Create your models here.

class HotelSearch(models.Model):
    city = models.CharField(max_length = 100, blank=True)
    checkin = models.DateField(default = timezone.now())
    checkout = models.DateField(default = timezone.now())
    type = models.CharField(max_length = 140)

    def __str__(self):
        return str(self.city)

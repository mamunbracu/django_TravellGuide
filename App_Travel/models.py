from django.db import models
from django.conf import settings
# Create your models here.

class Destination(models.Model):
    images = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=50, blank=True)
    price = models.FloatField()
    place = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50, blank=True)



class HotelList(models.Model):
    images = models.ImageField(upload_to='pics_hotel')
    name = models.CharField(max_length=50, blank=True)
    place = models.CharField(max_length=50, blank=True)
    price = models.FloatField()
    review = models.IntegerField(default=1)




class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True)
    contact = models.CharField(max_length=30)
    place = models.CharField(max_length=50)
    prefer_hotel = models.CharField(max_length=50, blank=False)

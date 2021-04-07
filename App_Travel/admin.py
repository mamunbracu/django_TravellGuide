from django.contrib import admin
from App_Travel.models import Destination, HotelList, Booking
# Register your models here.

admin.site.register(Destination)
admin.site.register(HotelList)
admin.site.register(Booking)
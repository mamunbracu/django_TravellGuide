from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from App_Travel.models import Destination, HotelList
from App_Travel.forms import BookingForm
# Create your views here.


def index(request):
    dest = Destination.objects.all()
    hotelList = HotelList.objects.all()
    return render(request, 'index.html', {'dest':dest, 'hotelList':hotelList}) 


def booking(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST, user=request.user)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = requuest.user
            obj.save()
            return HttpResponseRedirect(reverse('index.html'))
    return render(request, 'App_Travel/booking.html', context={'form':form})

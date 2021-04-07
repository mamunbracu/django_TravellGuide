from django.forms import ModelForm
from django import forms
from App_Travel.models import Booking


class BookingForm(ModelForm):
    name = forms.CharField(label="Your Name", widget=forms.TextInput(attrs={'placeholder':'Enter Your Name'}))
    email = forms.EmailField(label="Your Email", widget=forms.TextInput(attrs={'placeholder':'Enter Your Email'}))
    contact = forms.CharField(label="Your Contact", widget=forms.TextInput(attrs={'placeholder':'Enter Phone Number'}))
    place = forms.CharField(label="Where To Go", widget=forms.TextInput(attrs={'placeholder':'Enter The place name'}))
    prefer_hotel = forms.CharField(required=False, label="Prefer Hotel", widget=forms.TextInput(attrs={'placeholder':'Have any hotel Choice?'}))

    class Meta:
        model = Booking
        fields = ('name', 'email', 'contact', 'place', 'prefer_hotel')
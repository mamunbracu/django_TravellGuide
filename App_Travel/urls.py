from django.urls import path
from App_Travel import views

app_name = 'App_Travel'

urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.booking, name='booking')
   
]
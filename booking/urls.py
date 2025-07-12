from django.contrib import admin
from django.urls import path

from booking.views import room_list, booking

urlpatterns = [
    path('', room_list, name='room-list'),
    path('booking/<id_room>', booking, name='booking')
]
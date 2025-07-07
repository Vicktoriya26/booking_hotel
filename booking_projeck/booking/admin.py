from django.contrib import admin

from booking.models import Reservation, Room, TypeRoom

admin.site.register(TypeRoom)
admin.site.register(Room)
admin.site.register(Reservation)



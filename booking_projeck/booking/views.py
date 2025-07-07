from django.shortcuts import render , get_object_or_404

from booking.forms import BookingForm
from booking.models import Room


def room_list(request):
    rooms=Room.objects.all()
    context={
        'rooms':rooms
    }
    return render(request, 'room_list.html', context)

def booking(request, id_room):
    room = get_object_or_404(Room,id = id_room)
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.room = room
            reservation.reservator = request.user
            reservation.save()
    context = {
        'room' : room,
        'form' : form,
        
    }
    return render(request, template_name='booking.html', context=context)

    
    

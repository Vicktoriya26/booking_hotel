from django import forms

from booking.models import Reservation 

class BookingForm(forms.ModelForm):
    class Meta :
        model = Reservation
        fields = [
            'date_start',
            'date_end',
            'phone',
            'persons'
        ]
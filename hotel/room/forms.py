from django.forms import ModelForm
from .models import BookRoom
from django import forms


class BookRoomForm(ModelForm):
    booking_arrival = forms.DateField()
    booking_departure = forms.DateField()

    class Meta:
        model = BookRoom
        fields = [
            'booking_email', 'booking_arrival', 'booking_departure', 'no_of_guests', 'room'
        ]

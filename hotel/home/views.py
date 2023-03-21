from django.shortcuts import render
from room.models import Room, SpecialOffer
from room.forms import BookRoomForm

# Create your views here.


def index(request):
    rooms = Room.objects.all()
    offer = SpecialOffer.objects.all()
    book_room_form = BookRoomForm()
    context = {
        'rooms': rooms,
        'offer': offer,
        'form': book_room_form,
    }
    return render(request, "home.html", context)


def about_us(request):
    return render(request, "about.html")


def testimonial(request):
    return render(request, "testimonial.html")


def contact_us(request):
    return render(request, "contact.html")

from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, BookRoom, SpecialOffer
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import BookRoomForm
from django.contrib import messages

# Create your views here.


def index(request):
    room_list = Room.objects.all()
    paginator = Paginator(room_list, 4)
    page = request.GET.get('page', 1)
    book_room_form = BookRoomForm()

    try:
        rooms = paginator.page(page)
    except PageNotAnInteger:
        rooms = paginator.page(1)
    except EmptyPage:
        rooms = paginator.page(paginator.num_pages)

    context = {
        'rooms_list': rooms,
        'form': book_room_form,
    }
    return render(request, "room.html", context)


def room_detail(request, room_slug):
    room = get_object_or_404(Room, room_slug=room_slug)
    rooms = Room.objects.exclude(room_slug=room_slug)
    book_room_form = BookRoomForm()

    context = {
        'room': room,
        'form': book_room_form,
        'rooms': rooms,
    }
    return render(request, 'room_detail.html', context)


def book_room(request):
    book_room_form = BookRoomForm()

    context = {'form': book_room_form}

    if request.method == "POST":
        book_form_values = BookRoomForm(request.POST, None)
        if book_form_values.is_valid():
            ''' getting the cleaned data from the user '''
            customer_email = book_form_values.cleaned_data['booking_email']
            guests = book_form_values.cleaned_data['no_of_guests']
            arrival = book_form_values.cleaned_data['booking_arrival']
            room_book_chosen = book_form_values.cleaned_data['room']
            room_depart = book_form_values.cleaned_data['booking_departure']

            booking = BookRoom()  # making an instance of the model BookRoom
            book_a_room = booking.room_has_been_booked(customer_email, arrival, room_depart, guests, room_book_chosen)
            if book_a_room is False:
                messages.info(request, 'This room has been checked in. Please select another room of choice.')
                return redirect('rooms:book')
            messages.success(request, 'This room is available!.')
            return redirect('rooms:book')
    else:
        return render(request, 'book_room.html', context)


def special_room(request, special_slug):
    offer = get_object_or_404(SpecialOffer, special_slug=special_slug)
    context = {
        'offer': offer,
    }
    return render(request, 'vip.html', context)

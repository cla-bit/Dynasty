from .views import index, room_detail, book_room, special_room
from django.urls import path

app_name = "rooms"

urlpatterns = [
    path('view/', index, name='room'),
    path('room-detail/<slug:room_slug>/', room_detail, name='room_detail'),
    path('book-a-room/', book_room, name='book'),
    path('vip/<slug:special_slug>/', special_room, name='vip'),
]

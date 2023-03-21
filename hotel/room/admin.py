from django.contrib import admin
from .models import RoomFeature, Room, RoomSmallImage, SpecialOffer, BookRoom

# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room']
    prepopulated_fields = {'room_slug': ('room',)}


@admin.register(RoomFeature)
class RoomFeatureAdmin(admin.ModelAdmin):
    list_display = ['room_feature_title']


@admin.register(RoomSmallImage)
class RoomSmallImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'room_img']


@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
    list_display = ['special_title', 'price']
    prepopulated_fields = {'special_slug': ('special_title',)}


@admin.register(BookRoom)
class BookRoomAdmin(admin.ModelAdmin):
    list_display = ['booking_email', 'booking_arrival', 'booking_departure', 'no_of_guests', 'room']

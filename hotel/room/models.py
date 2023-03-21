from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class RoomSmallImage(models.Model):
    room_img = models.ImageField(upload_to='room/small')

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Room Small Images'


class RoomFeature(models.Model):
    room_feature_title = models.CharField(max_length=20, verbose_name='Room Feature', null=True, blank=True)
    room_feature_desc = models.TextField(verbose_name='Room Feature Description')

    class Meta:
        verbose_name_plural = 'Room Features'

    def __str__(self):
        return self.room_feature_title


class Room(models.Model):
    ROOM_CHOICE = [
        ('Single Room', 'Single Room'), ('Double Room', 'Double Room'),
        ('Premiere Room', 'Premiere Room'), ('Deluxe Room', 'Deluxe Room'),
        ('EnSuite Room', 'EnSuite Room'), ('Master EnSuite Room', 'Master EnSuite Room')
    ]
    room = models.CharField(max_length=30, default='Single Room', choices=ROOM_CHOICE, verbose_name='Room')
    room_slug = models.CharField(max_length=30, verbose_name='Room Slug', unique=True)
    room_description = models.TextField(verbose_name='Room Description')
    room_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Room Price')
    room_small_description = models.TextField(verbose_name='Additional Description')
    room_big_img = models.ImageField(upload_to='room', verbose_name='Room Big Image')
    room_small_img = models.ManyToManyField(RoomSmallImage, related_name='rooms_img', verbose_name='Room Small Image')
    room_feature = models.ManyToManyField(RoomFeature, related_name='rooms_feature')

    class Meta:
        ordering = ['room']
        indexes = [
            models.Index(fields=['room', 'room_slug']),
            models.Index(fields=['room_description']),
            models.Index(fields=['room_price'])
        ]
        verbose_name_plural = 'Rooms'

    def __str__(self):
        return self.room

    def get_absolute_url(self):
        return reverse('rooms:room_detail', args=[self.room_slug])


class SpecialOffer(models.Model):
    image = models.ImageField(upload_to='special')
    special_title = models.CharField(max_length=10, verbose_name='Title', null=True, blank=True)
    special_slug = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Price')

    class Meta:
        ordering = ['special_title']
        indexes = [
            models.Index(fields=['special_title', 'special_slug']),
            models.Index(fields=['price'])
        ]
        verbose_name_plural = 'Special Offers'

    def __str__(self):
        return self.special_title

    def get_absolute_url(self):
        return reverse('rooms:vip', args=[self.special_slug])


class BookRoom(models.Model):
    class Guest(models.IntegerChoices):
        One = 1
        Two = 2
        Three = 3
        Four = 4

    booking_email = models.EmailField(verbose_name='Email', null=True)
    booking_arrival = models.DateField(verbose_name='Arrival', null=True)
    booking_departure = models.DateField(verbose_name='Departure', null=True)
    no_of_guests = models.IntegerField(choices=Guest.choices, verbose_name='Number of Guests')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Room Choice')

    class Meta:
        ordering = ['booking_arrival']
        indexes = [
            models.Index(fields=['booking_email']),
            models.Index(fields=['booking_arrival', 'booking_departure'])
        ]

    def __str__(self):
        return f'{self.booking_email}, {self.room}'

    def room_has_been_booked(self, email, arrival_date, depart_date, guest, room_chosen):
        date_now = timezone.now().date()
        print(f'Now in number of days: {date_now.day} days')  # result will be 14

        date_future = timezone.timedelta(days=date_now.day)
        ''' the result will give 14 days, 0:00:00 '''
        print(date_future)

        ''' The current data input gotten from the form '''
        self.room_chosen = room_chosen  # know the room selected
        self.booking_departure = depart_date  # know the date of departure
        self.current_depart_duration_days = depart_date.day - arrival_date.day  # know the duration of stay in days
        self.booking_email = email  # the user email
        self.booking_arrival = arrival_date  # know the date of arrival
        self.no_of_guests = guest  # know the number of guests

        print(f'Date Now: {date_now}')  # result will be the current date
        print(f'Arrival date: {self.booking_arrival}')  # result will be date of arrival
        print(f'Depart Date: {self.booking_departure}')  # result will be date of departure

        print(f'Duration of stay: {self.current_depart_duration_days}')
        print(f'Room: {self.room_chosen}')
        print(f'Timedelta: {timezone.timedelta(days=self.current_depart_duration_days)}')

        print(f'Departing no of days: {self.current_depart_duration_days}')
        print(f'Depart in days: {self.booking_departure.day} day')

        print(f'Date now + Timedelta (current): '
              f'{date_now + timezone.timedelta(days=self.current_depart_duration_days)}')
        # this is the future date from today

        try:
            if BookRoom.objects.filter(room=room_chosen).exists():
                print(f'This room {self.room_chosen} exists')  # return a message
                room_booking = BookRoom.objects.filter(room=room_chosen).last()  # return the last room booked
                print(f'This is the last room booking date departure: {room_booking.booking_departure}')
                print(f'This is the no of guests in the last room booked: {room_booking.no_of_guests}')

                ''' compare the new arrival input with the last recorded depart date of the same room'''
                if self.booking_arrival <= room_booking.booking_departure:
                    print(f'Room is still in use and will be free in '
                          f'{room_booking.booking_departure.day - date_now.day} days: '
                          f'{room_booking.booking_departure}')
                    return False
                else:
                    print(f'This room {self.room_chosen} is free')
                    book_a_room = BookRoom.objects.create(
                        booking_email=self.booking_email, booking_arrival=self.booking_arrival,
                        booking_departure=self.booking_departure, no_of_guests=self.no_of_guests,
                        room=self.room_chosen
                    )
                    book_a_room.save()
                    return True
        except BookRoom.DoesNotExist:
            print('Booking of this room does not exist')





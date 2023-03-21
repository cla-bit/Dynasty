from .models import Room


def room(request):
    return {
        'rooms': Room.objects.all(),
    }

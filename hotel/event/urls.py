from .views import index
from django.urls import path

app_name = "events"

urlpatterns = [
    path('space/', index, name='event_space'),
]
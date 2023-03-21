from .views import index
from django.urls import path

app_name = "restaurants"

urlpatterns = [
    path('view/', index, name='restaurant_space'),
]
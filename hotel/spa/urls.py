from .views import index
from django.urls import path

app_name = "spa"

urlpatterns = [
    path('view/', index, name='spa'),
]
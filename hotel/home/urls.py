from .views import index, about_us, testimonial, contact_us
from django.urls import path

app_name = "home"

urlpatterns = [
    path('', index, name='home'),
    path('about-us/', about_us, name='about'),
    path('reviews/', testimonial, name='testimony'),
    path('contact-us/', contact_us, name='contact'),
]
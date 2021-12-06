from django.urls import path
from .views import HotelSerializerView, DriverSerializerView, TripSerializerView

urlpatterns = [
    path('', TripSerializerView.as_view()),
    path('drivers/',DriverSerializerView.as_view()),
    path('hotels/',HotelSerializerView.as_view()),
]
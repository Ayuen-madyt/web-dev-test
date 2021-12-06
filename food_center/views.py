import json
from rest_framework import generics
from .models import Hotel,Driver,Trip
from .serializers import HotelSerializer,DriverSerializer,TripSerializer

# Create your views here.
class HotelSerializerView(generics.ListAPIView):
    with open('files/hotels.json') as hotel_data:
        hotels = json.load(hotel_data)
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class DriverSerializerView(generics.ListAPIView):
    with open('files/drivers.json') as driver_data:
        drivers = json.load(driver_data)
        # print(drivers)
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class TripSerializerView(generics.ListAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    
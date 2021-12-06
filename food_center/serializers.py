from rest_framework import serializers
from .models import Driver,Hotel,Trip

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = "__all__"
    
class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['time_range','rating','driver','hotel']
    
class DriverSerializer(serializers.ModelSerializer):
    trips = TripSerializer(many=True, read_only=True)
    class Meta:
        model = Driver
        fields = ['id','first_name','last_name','trips']

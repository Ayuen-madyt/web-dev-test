import json
from django.core.management.base import BaseCommand
from food_center.models import Trip
from food_center.models import Driver
from food_center.models import Hotel

class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('files/drivers.json') as f:
            data_list = json.load(f)
            # print(data_list)

        for data in data_list:
            f_name = data['first_name']
            l_name = data['last_name']
            uuid = data['uuid']
            Driver.objects.get_or_create(id=uuid,first_name=f_name,last_name=l_name)
        
    def handle(self, *args, **options):
        with open('files/hotels.json') as f:
            data_list = json.load(f)

        for data in data_list:
            name = data['name']
            address = data['address']
            uuid = data['uuid']
            Hotel.objects.get_or_create(id=uuid,name=name,address=address)

    def handle(self, *args, **options):
        with open('files/trips.json') as f:
            data_list = json.load(f)

        for data in data_list:
            driver_id = data['driver_id']
            hotel_id = data['hotel_id']
            start_time = data['start_time']
            delivery_time = data['delivery_time']
            rating = data['rating']
            Trip.objects.get_or_create(driver_id=driver_id,hotel_id=hotel_id,start_time=start_time,delivery_time=delivery_time,rating=rating)
    
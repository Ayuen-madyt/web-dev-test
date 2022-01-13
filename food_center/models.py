from django.db import models
import uuid

# Create your models here.
class Driver(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False
        )
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Hotel(models.Model):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False
        )
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    
class Trip(models.Model):
    driver = models.ForeignKey(
                Driver,
                null=True,
                blank=True,
                on_delete=models.CASCADE,
            )
    hotel = models.ForeignKey(
                Hotel,
                null=True,
                blank=True,
                on_delete=models.CASCADE,
            )
    start_time = models.DateTimeField(auto_now_add=True)
    delivery_time = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=5,decimal_places=2)

    class Meta:
        ordering = ['-start_time']

    # time range is the difference btwn st
    @property
    def time_range(self):
        return self.delivery_time - self.start_time


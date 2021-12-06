from django.contrib import admin
from .models import Hotel,Driver,Trip

# Register your models here.
admin.site.register(Trip)
admin.site.register(Hotel)
admin.site.register(Driver)
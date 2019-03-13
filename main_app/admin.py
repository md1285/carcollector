from django.contrib import admin
from .models import Car, Fillup, Driver

# Register your models here.
admin.site.register(Car)
admin.site.register(Fillup)
admin.site.register(Driver)
from django.db import models
from django.urls import reverse
from datetime import datetime

GAS_STATIONS = (
    ('S', 'Shell'),
    ('B', 'BP'),
    ('C', 'Chevron'),
)

class Driver(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'
    def get_absolute_url(self):
        return reverse('driver_detail', kwargs={'driver_id': self.id})


# Create your models here.
class Car(models.Model):
    color = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    year = models.IntegerField()
    drivers = models.ManyToManyField(Driver)
    def __str__(self):
        return f'{self.year} {self.make} {self.style}'
    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})
    def enough_fillups(self):
        return self.fillup_set.filter(date__month=datetime.now().month).count() >= 3

class Fillup(models.Model):
    date = models.DateField('fillup date')
    cost = models.IntegerField(default=0)
    gas_station = models.CharField(
        max_length=1,
        choices=GAS_STATIONS,
        default=GAS_STATIONS[0][0],
    )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.get_gas_station_display()} for ${self.cost} on {self.date}'
    class Meta:
        ordering = ['-date']
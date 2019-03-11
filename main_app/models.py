from django.db import models

# Create your models here.
class Car(models.Model):
    color = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    driver = models.CharField(max_length=100)
    year = models.IntegerField()
    def __str__(self):
        return f'{self.year} {self.make} {self.style}'
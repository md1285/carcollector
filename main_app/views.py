from django.shortcuts import render
from django.http import HttpResponse

class Car():
    def __init__(self, color, engine, make, model, driver, year):
        self.color = color
        self.engine = engine
        self.make = make
        self.model = model
        self.driver = driver
        self.year = year

cars = [
    Car('red', 'V6', 'Honda', 'Civic', 'Sam', 2004),
    Car('yellow', 'V8', 'Toyota', 'Carolla', 'John', 2012),
    Car('blue', 'hamster running on a stationary wheel', 'Ford', 'Taurus', 'Sally', 2020),
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

def cars_index(request):
    return render(request, 'cars/index.html', {'cars': cars})
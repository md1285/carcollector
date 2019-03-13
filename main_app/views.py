from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Car, Driver
from .forms import FillupForm

# Create your views here.

def drivers_index(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers/index.html', {'drivers': drivers})

def driver_detail(request, driver_id):
    driver = Driver.objects.get(id=driver_id)
    return render(request, 'drivers/detail.html', {'driver': driver})

class DriverCreate(CreateView):
    model = Driver
    fields = '__all__'

class DriverUpdate(UpdateView):
    model = Driver
    fields = '__all__'

class DriverDelete(DeleteView):
    model = Driver
    success_url = '/drivers/'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

def cars_index(request):
    cars = Car.objects.order_by('-year')
    return render(request, 'cars/index.html', {'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/detail.html', {
        'car': car,
        'fillup_form': FillupForm() 
    })

class CarCreate(CreateView):
    model = Car
    fields = ['year', 'make', 'style', 'color', 'engine']

class CarUpdate(UpdateView):
    model = Car
    fields = ['year', 'color', 'driver', 'engine']

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'

def add_fillup(request, car_id):
    form = FillupForm(request.POST)
    if form.is_valid():
        form = form.save(commit=False)
        form.car_id = car_id
        form.save()
    return redirect('detail', car_id=car_id)

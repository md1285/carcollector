from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Car
from .forms import FillupForm

# Create your views here.

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
    fields = ['year', 'make', 'style', 'color', 'driver', 'engine']

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

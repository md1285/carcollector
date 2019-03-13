from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # drivers
    path('drivers/', views.drivers_index, name = 'drivers_index'),
    path('drivers/<int:driver_id>/', views.driver_detail, name = 'driver_detail'),
    path('drivers/create/', views.DriverCreate.as_view(), name = 'drivers_create'),
    path('drivers/<int:pk>/update/', views.DriverUpdate.as_view(), name = 'drivers_update'),
    path('drivers/<int:pk>/delete/', views.DriverDelete.as_view(), name = 'drivers_delete'),

    # cars
    path('cars/', views.cars_index, name='index'),
    path('cars/<int:car_id>/', views.car_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/add_fillup/', views.add_fillup, name='add_fillup'),
]
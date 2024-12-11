from django.shortcuts import render,get_list_or_404
from .models import *

def index(request):
    brand = Brand.objects.all()
    cars = Car.objects.all()
    return render(request,'index.html',{'brand':brand, 'cars':cars})

def brand_cars(request, brand_id):
    brand = get_list_or_404(Brand, id=brand_id)
    cars = Brand.cars.all()
    return render(request,'brand_cars.html',{'brand':brand,'cars':cars})

def car_detail(request, car_id):
    car = get_list_or_404(Car, id=car_id)
    return render(request, 'car_detail.html', {'car': car})

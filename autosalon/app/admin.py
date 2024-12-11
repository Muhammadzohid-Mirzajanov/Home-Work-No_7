from django.contrib import admin
from .models import Brand,Car

@admin.register(Brand)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price')
    list_filter = ('brand',)

from django.contrib import admin

from .models import Car, CarBrand, CarModel, CarColor


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('pk', 'car_brand', 'car_model', 'car_register_number',)
    search_fields = ('car_register_number',)


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('brand',)
    search_fields = ('brand',)


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('model',)
    search_fields = ('model',)


@admin.register(CarColor)
class CarColorAdmin(admin.ModelAdmin):
    list_display = ('color',)
    search_fields = ('color',)

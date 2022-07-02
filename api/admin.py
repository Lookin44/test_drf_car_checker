from django.contrib import admin

from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('pk', 'car_brand', 'car_model', 'car_register_number',)
    search_fields = ('car_register_number',)

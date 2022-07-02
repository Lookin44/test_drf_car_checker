from django.db import models


class Car(models.Model):
    """Модель описывающая автомобиль для постановки на учет в базу."""
    car_brand = models.CharField(max_length=255)
    car_model = models.CharField(max_length=255)
    car_color = models.CharField(max_length=255)
    car_register_number = models.CharField(max_length=9, unique=True)
    car_create_date = models.IntegerField()
    car_vin = models.CharField(max_length=17, unique=True)
    car_sts_number = models.CharField(max_length=10, unique=True)
    car_sts_date = models.DateField()
    car_date_add = models.DateTimeField(auto_now_add=True)
    car_date_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.car_vin}, {self.car_model}, {self.car_color}'

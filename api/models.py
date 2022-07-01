from django.db import models


class CarColor(models.Model):
    """Модель для цвета. Так как в ГИБДД есть список определенных
    цветов, лучше занести его в БД. В дальнейшем это позволит
    избежать дублирование цвета: БЕЛЫЙ, Белый, белый и т.д."""
    color = models.CharField(unique=True, max_length=255, db_index=True)

    def __str__(self):
        return self.color


class CarBrand(models.Model):
    """Модель для марки автомобиля. В дальнейшем это позволит
    избежать дублирование цвета: SKODA, Skoda, skoda и т.д."""
    brand = models.CharField(max_length=255)

    def __str__(self):
        return self.brand


class CarModel(models.Model):
    """Модель для марки автомобиля. В дальнейшем это позволит
    избежать дублирование цвета: RAPID, Rapid, rapid и т.д."""
    model = models.CharField(max_length=255)

    def __str__(self):
        return self.model


class Car(models.Model):
    """Модель описывающая автомобиль для постановки на учет в базу."""
    car_brand = models.ForeignKey(
        'CarBrand', on_delete=models.PROTECT, related_name='cars'
    )
    car_model = models.ForeignKey(
        'CarModel', on_delete=models.PROTECT, related_name='cars'
    )
    car_color = models.ForeignKey(
        'CarColor', on_delete=models.PROTECT, related_name='cars'
    )
    car_register_number = models.CharField(max_length=9, unique=True)
    car_create_date = models.IntegerField()
    car_vin = models.CharField(max_length=17, unique=True)
    car_sts_number = models.CharField(max_length=10, unique=True)
    car_sts_date = models.DateField()
    car_date_add = models.DateTimeField(auto_now_add=True)
    car_date_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.car_vin}, {self.car_model}, {self.car_color}'

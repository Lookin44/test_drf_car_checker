from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Car, CarBrand


class CarBrandSerializer(ModelSerializer):

    class Meta:
        model = CarBrand
        fields = '__all__'


class CarSerializer(ModelSerializer):
    car_brand = serializers.CharField(read_only=True, source='car_brand.brand')
    car_model = serializers.CharField(read_only=True, source='car_model.model')
    car_color = serializers.CharField(read_only=True, source='car_color.color')

    class Meta:
        model = Car
        fields = '__all__'

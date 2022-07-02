from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Car


class CarSerializer(ModelSerializer):

    class Meta:
        model = Car
        fields = (
            'car_brand',
            'car_model',
            'car_color',
            'car_register_number',
            'car_create_date',
            'car_vin',
            'car_sts_number',
            'car_sts_date',
        )


class FileUploadSerializer(serializers.Serializer):

    file = serializers.FileField()

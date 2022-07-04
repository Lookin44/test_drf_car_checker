import datetime as dt

import pandas as pd
from django.http import HttpResponse
from rest_framework import mixins, filters, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Car
from .serializers import (
    CarSerializer,
    FileUploadSerializer,
)


class CarViewSet(mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 GenericViewSet):
    """Представление обрабатывающее Get, Put и Post запросы согласно тз.
    Выводятся только основные значения, так как в БД есть значения
    для дальнейшего развития приложения (время создания записи и время
    ее изменения), но на текущий момент они не требуются. """
    search_fields = (
        'car_brand',
        'car_model',
        'car_color',
        'car_register_number',
        'car_create_date',
        'car_vin',
        'car_sts_number',
        'car_sts_date',
    )
    filter_backends = (filters.SearchFilter,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticated,)


class UploadFileView(CreateAPIView):
    """Представление отвечающее за импорт csv и xlsx таблицы в БД. """
    serializer_class = FileUploadSerializer

    def post(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']

        _dict_file_obj = request.data['file'].__dict__

        try:
            if _dict_file_obj['_name'].endswith('.csv'):
                reader = pd.read_csv(file)
            elif _dict_file_obj['_name'].endswith('.xlsx'):
                reader = pd.read_excel(file)
            else:
                return Response(
                    {
                        "error": "Файл не поддерживается. "
                                 "Поддерживаемые файлы scv и xlsx"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            for _, row in reader.iterrows():
                new_file = Car(
                    car_brand=row['car_brand'],
                    car_model=row['car_model'],
                    car_color=row['car_color'],
                    car_register_number=row['car_register_number'],
                    car_create_date=row['car_create_date'],
                    car_vin=row['car_vin'],
                    car_sts_number=row['car_sts_number'],
                    car_sts_date=row['car_sts_date']
                )
                new_file.save()
            return Response({"status": "Загружено"},
                            status.HTTP_201_CREATED)
        except Exception:
            return Response({"status": "Что то пошло не так."},
                            status.HTTP_400_BAD_REQUEST)


class DownloadFileViewSet(APIView):
    """Представление для сохранения базы в csv и xlsx формате."""

    def get(self, request):
        file_name = dt.datetime.today().strftime('%d-%m-%Y')

        serializer = CarSerializer(Car.objects.all(), many=True)
        dataframe = pd.DataFrame(serializer.data)
        if request.data['format'] == 'csv':
            response = HttpResponse(
                content_type='text/csv',
                headers={
                    'Content-Disposition': 'attachment; '
                                           f'filename="{file_name}.csv"'}
            )
            dataframe.to_csv(response)
        elif request.data['format'] == 'xlsx':
            response = HttpResponse(
                content_type='text/xlsx',
                headers={
                    'Content-Disposition': 'attachment; '
                                           f'filename="{file_name}.xlsx"'}
            )
            dataframe.to_excel(response)
        else:
            return Response({"status": "Не поддерживаемый формат."},
                            status.HTTP_400_BAD_REQUEST)
        return response

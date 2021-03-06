# DRF API_CAR_DATABASE
***

Тестовое API-приложение для ведения учета автомобилей
# Задание:
- аутентификация с использованием имени пользователя и пароля;
- создания/редактирования/поиск записей ТС (транспортное средство);
- загрузки и выгрузки списка записей ТС в/из файлов формата csv, xlsx;
- авторизация доступа к методам АПИ.

Приложение должно состоять из набора веб-АПИ, работающего по REST.
Приложение не должно содержать интерфейса.
Модель ТС состоит из следующих полей:
- Марка
- Модель
- Цвет
- Регистрационный номер
- Год выпуска
- vin
- Номер СТС (свидетельство о регистрации)
- Дата СТС

# Реализация:
> ## Стэк:
> - Python 3.10
> - Django 4.0.5
> - Django REST Framework 3.13.1
> - Djoser 2.1.0
> - Pandas 1.4.3

## Установка:

Скопируйте репозиторий на свой компьютер:
```shell
https://github.com/Lookin44/test_drf_car_checker
```

Зайдите в скачанную директорию, установите виртуальное окружение, активируйте его и установите зависимости:
```shell
python3 -m venv venv && source venv/bin/activate && pip3 install -r requirements.txt
```

Создайте миграцию, выполните ее и запустите сервер:
```shell
python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver
```

У Вас создастся локальная база данных SQLite. В нее будут помещаться все данный об автомобилях.
Далее для работы с API-приложением необходимо создать пользователя, 
для этого необходимо отправить POST-запрос на энедпоинт: 
>http://127.0.0.1:8000/api/auth/users/

с телом:

```json
{
  "username": "Ваш ник",
  "password": "Придумайте пароль"
}
```
Вы создали пользователя, теперь Вам необходимо создать Token который будет передаваться в Header-запроса,
так сервер будет понимать кто к нему обращается, для этого отправьте POST-запрос на эндпоинт: 
> http://127.0.0.1:8000/api/auth/token/login/ 

с предыдущим телом:
```json
{
  "username": "Ваш ник",
  "password": "Придумайте пароль"
}
```

В ответ Вам вернется токен:
```json
{"auth_token":"0ef9ae8714f33a2a5d1c2077edfd508f9e0d157b"}
```

В последующие запросы добавьте в Header-запроса новый параметр:
```json
{"Authorization": "Token 0ef9ae8714f33a2a5d1c2077edfd508f9e0d157b"} # Вставте токен который вернулся Вам
```

Сейчас база данных пуста, поэтому можете ее заполнить из csv файла, который лежит в репозитории.
Отправьте POST-запросом файл test_base.csv на эндпоинт: 
> http://127.0.0.1:8000/api/v1/upload/

с телом:
```json
{
  "file": Отправляемый файл
}
```

Теперь в базу занесены автомобили, что бы увидеть их список отправьте GET-запрос на эндпоинт:
> http://127.0.0.1:8000/api/v1/car/

Эндпоинт вернет Вам список всех автомобилей в БД. Для поиска определенного автомобиля передайте 
GET-запрос на эндпоинт с параметром search
> http://127.0.0.1:8000/api/v1/car/?search= {искомый параметр}
>
> ПРИМЕР: http://127.0.0.1:8000/api/v1/car/?search=БЕЛЫЙ # Выдаст все белые автомобили

Искомым параметром, может быть: 
- брэнд, 
- модель, 
- цвет, 
- регистрационный номер,
- дата создания автомобиля,
- Вин номер,
- Номер СТС,
- Дата СТС

Для создания записи о новом автомобиле передайте POST-запрос на эндпоинт:
> http://127.0.0.1:8000/api/v1/car/

с телом
```json
{
    "car_brand": "NISSAN",
    "car_model": "ALMERA",
    "car_color": "КРАСНЫЙ",
    "car_register_number": "T897KC29",
    "car_create_date": 2010,
    "car_vin": "KL1TD56626B697413",
    "car_sts_number": "78CX892147",
    "car_sts_date": "2015-05-14"
}
```
Запись создана, Вам вернется ответ в виде
```json
{
    "id": 13,
    "car_brand": "NISSAN",
    "car_model": "ALMERA",
    "car_color": "КРАСНЫЙ",
    "car_register_number": "T897KC29",
    "car_create_date": 2010,
    "car_vin": "KL1TD56626B697413",
    "car_sts_number": "78CX892147",
    "car_sts_date": "2015-05-14"
}
```
Для изменения записи отправьте PATCH-запрос на эндпоинт:
> http://127.0.0.1:8000/api/v1/car/13/ # В данном случае мы меняем автомобиль с индефикатором 13 (тоже который мы только что создали)

с телом

```json
{
  "car_color": "КРАСНЫЙ" # В данном случае мы меняем цвет автомобиля
}
```

После создания нескольких автомобилей, если есть необходимость выгрузки базы в csv или xlsx формате
отправьте GET-запрос на эндпоинт:
> http://127.0.0.1:8000/api/v1/download/

с телом:
```json
{
  "format": "csv"
}
# или 
{
  "format": "xlsx"
}
```
После того ка Вы выполнили свою работу с API-приложением, для выхода из системы отправьте POST-запрос на эндпоинт:
> http://127.0.0.1:8000/api/auth/token/logout/

Ваш токен больше не работает.
***

### Спасибо, что прочитали инструкцию до конца.

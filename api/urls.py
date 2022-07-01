from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CarViewSet


router_v1 = SimpleRouter()
router_v1.register(r'car', CarViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]

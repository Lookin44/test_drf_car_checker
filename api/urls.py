from django.urls import include, path, re_path
from rest_framework.routers import SimpleRouter

from .views import CarViewSet, UploadFileView


router_v1 = SimpleRouter()
router_v1.register('car', CarViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('upload/', UploadFileView.as_view()),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken'))
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TotalAssaultViewSet

router = DefaultRouter()
router.register(r'TotalAssault', TotalAssaultViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

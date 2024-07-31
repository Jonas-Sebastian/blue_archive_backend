from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TotalAssaultViewSet, GrandAssaultViewSet, CategoryViewSet, StudentViewSet

router = DefaultRouter()
router.register(r'TotalAssault', TotalAssaultViewSet)
router.register(r'GrandAssault', GrandAssaultViewSet)
router.register(r'Categories', CategoryViewSet)
router.register(r'Students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

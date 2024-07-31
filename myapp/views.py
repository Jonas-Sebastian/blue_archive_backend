from django.shortcuts import render
from rest_framework import viewsets
from .models import TotalAssault, GrandAssault, Category, Student
from .serializers import TotalAssaultSerializer, GrandAssaultSerializer, CategorySerializer, StudentSerializer

class TotalAssaultViewSet(viewsets.ModelViewSet):
    queryset = TotalAssault.objects.all()
    serializer_class = TotalAssaultSerializer

class GrandAssaultViewSet(viewsets.ModelViewSet):
    queryset = GrandAssault.objects.all()
    serializer_class = GrandAssaultSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
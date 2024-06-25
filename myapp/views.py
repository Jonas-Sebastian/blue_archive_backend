from django.shortcuts import render
from rest_framework import viewsets
from .models import TotalAssault
from .serializers import TotalAssaultSerializer

class TotalAssaultViewSet(viewsets.ModelViewSet):
    queryset = TotalAssault.objects.all()
    serializer_class = TotalAssaultSerializer

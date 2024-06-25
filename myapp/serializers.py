from rest_framework import serializers
from .models import TotalAssault
from .models import GrandAssault

class TotalAssaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalAssault
        fields = ['id', 'name']

class GrandAssaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrandAssault
        fields = ['id', 'name']
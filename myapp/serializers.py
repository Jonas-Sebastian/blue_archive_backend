from rest_framework import serializers
from .models import TotalAssault
from .models import GrandAssault

class TotalAssaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalAssault
        fields = ['id', 'name']

class GrandAssaultSerializer(serializers.ModelSerializer):
    color_display = serializers.CharField(source='get_color_display', read_only=True)

    class Meta:
        model = GrandAssault
        fields = ['id', 'name', 'color', 'color_display']
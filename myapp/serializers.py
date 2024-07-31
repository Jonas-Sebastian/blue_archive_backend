from rest_framework import serializers
from .models import TotalAssault, GrandAssault, Category, Student

class TotalAssaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TotalAssault
        fields = ['id', 'name']

class GrandAssaultSerializer(serializers.ModelSerializer):
    color_display = serializers.CharField(source='get_color_display', read_only=True)

    class Meta:
        model = GrandAssault
        fields = ['id', 'name', 'color', 'color_display']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class StudentSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'categories']
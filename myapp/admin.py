from django.contrib import admin
from .models import TotalAssault, GrandAssault, Category, Student

@admin.register(TotalAssault)
class TotalAssaultAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(GrandAssault)
class GrandAssaultAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'get_color_display')
    list_filter = ('color',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_categories', 'display_total_assaults', 'display_grand_assaults')
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ('categories', 'total_assaults', 'grand_assaults')

    def display_categories(self, obj):
        return ", ".join([cat.name for cat in obj.categories.all()])
    display_categories.short_description = 'Categories'

    def display_total_assaults(self, obj):
        return ", ".join([assault.name for assault in obj.total_assaults.all()])
    display_total_assaults.short_description = 'Total Assaults'

    def display_grand_assaults(self, obj):
        return ", ".join([assault.name for assault in obj.grand_assaults.all()])
    display_grand_assaults.short_description = 'Grand Assaults'

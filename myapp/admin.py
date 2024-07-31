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
    list_display = ('name', 'display_categories')
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ('categories',)  # Manages ManyToMany relationship in admin
    
    def display_categories(self, obj):
        return ", ".join([cat.name for cat in obj.categories.all()])
    display_categories.short_description = 'Categories'
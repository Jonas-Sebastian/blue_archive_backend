from django.contrib import admin
from .models import TotalAssault, GrandAssault

# Register TotalAssault
admin.site.register(TotalAssault)

# Register GrandAssault
@admin.register(GrandAssault)
class GrandAssaultAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'get_color_display')
    list_filter = ('color',)
    search_fields = ('name',)
    ordering = ('name',)
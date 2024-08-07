from django.contrib import admin
from .models import Todo
# Register your models here.

class Display_task(admin.ModelAdmin):
    list_display = ('task','is_completed','create_at','update_at')
    
admin.site.register(Todo,Display_task)
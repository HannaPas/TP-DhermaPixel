from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Servicios

# Register your models here.

@admin.register(Servicios)
class ServiciosAdmin(ModelAdmin):
    ...
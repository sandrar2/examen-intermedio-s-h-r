from django.contrib import admin
from .models import Meseros



@admin.register(Meseros)
class MeserosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad', 'nacionalidad', 'dni')

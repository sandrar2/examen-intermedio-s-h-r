from django.contrib import admin
from .models import Platos


#admin.site.register(Owner)
@admin.register(Platos)
class PlatosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'procedencia')


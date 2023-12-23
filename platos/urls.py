from django.urls import path
from . import views


urlpatterns = [
    path('platos_list/', views.platos_list, name='platos_list'),
    path('platillos_peru_mayor_40/', views.platillos_peru_mayor_40, name='platillos_peru_mayor_40'),
    path('eliminar_platos_menor_15/', views.eliminar_platos_menor_15, name='eliminar_platos_menor_15')
]


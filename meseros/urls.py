from django.urls import path
from . import views

urlpatterns = [
    path('meseros_list/', views.meseros_list, name='meseros_list'),
    path('meseros_peru_menor_30/', views.meseros_peru_menor_30, name='meseros_peru_menor_30'),
    path('actualizar_edades/', views.actualizar_edades, name='actualizar_edades')
]


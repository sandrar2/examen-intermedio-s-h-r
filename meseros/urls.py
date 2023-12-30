from django.urls import path
from . import views
from .views import EditarMeseroView, EliminarMeseroView
from .views import TuVistaProtegida, tu_vista_sin_proteccion
from .views import crear_mesero
from .views import EditarMeseroView
from .views import DetalleMeseroView
from .views import EliminarMeseroView
from .views import CrearMeseroView
from .views import MeserosPeruView

urlpatterns = [
    path('meseros_list/', views.meseros_list, name='meseros_list'),
    path('meseros_peru_menor_30/', views.meseros_peru_menor_30, name='meseros_peru_menor_30'),
    path('actualizar_edades/', views.actualizar_edades, name='actualizar_edades'),
    path('meseros_mayores_de_25/', views.meseros_mayores_de_25, name='meseros_mayores_de_25'),
    path('editar_mesero/<int:pk>/', EditarMeseroView.as_view(), name='editar_mesero'),
    path('eliminar_mesero/<int:pk>/', EliminarMeseroView.as_view(), name='eliminar_mesero'),
    path('tu_api/protegida/', TuVistaProtegida.as_view(), name='protegida'),
    path('tu_api/sin_proteccion/', tu_vista_sin_proteccion, name='sin_proteccion'),
    path('crear_mesero/', crear_mesero, name='crear_mesero'),
    path('editar_mesero/<int:pk>/', EditarMeseroView.as_view(), name='editar_mesero'),
    path('detalle_mesero/<int:pk>/', DetalleMeseroView.as_view(), name='detalle_mesero'),
    path('eliminar_mesero/<int:pk>/', EliminarMeseroView.as_view(), name='eliminar_mesero'),
    path('crear_mesero/', CrearMeseroView.as_view(), name='crear_mesero'),
    path('meseros_peru/', MeserosPeruView.as_view(), name='meseros_peru'),
]





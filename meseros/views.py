from django.shortcuts import render
from rest_framework import generics,permissions

from .models import Meseros
from .forms import MeseroForm
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import MeseroSerializer
from rest_framework import status

def meseros_list(request):
    data_context = {
        'nombre': 'Luis',
        'edad': 25,
        'nacionalidad': 'Peru',
        'dni': 12345678
    }
    return render(request, 'meseros_list.html', context=data_context)

def meseros_peru_menor_30(request):
    meseros_peru_menor_30 = Meseros.objects.filter(nacionalidad='Perú', edad__lt=30)

    data_context = {
        'meseros_peru_menor_30': meseros_peru_menor_30
    }

    return render(request, 'meseros_peru_menor_30.html', context=data_context)

def actualizar_edades(request):
    meseros = Meseros.objects.all()


    for meseros in meseros:
        meseros.edad += 5
        meseros.save()


    data_context = {
        'mensaje': 'Edades actualizadas correctamente.'
    }

    return render(request, 'actualizar_edades.html', context=data_context)


def meseros_mayores_de_25(request):
    meseros_mayores = Meseros.objects.filter(edad__gt=25)
    return render(request, 'meseros_mayores_de_25.html', {'meseros_mayores': meseros_mayores})

def meseros_peruanos(request):
    meseros_peruanos = Meseros.objects.filter(nacionalidad='peru')
    return render(request, 'meseros_peruanos.html', {'meseros_peruanos': meseros_peruanos})

def crear_mesero(request):
    crear_mesero = Meseros.objects.all()
    return render(request, 'crear_mesero.html', {'crear_mesero': crear_mesero})

class EditarMeseroView(UpdateView):
    model = Meseros
    form_class = MeseroForm
    template_name = 'editar_mesero.html'
    success_url = reverse_lazy('meseros_list')

class EliminarMeseroView(DeleteView):
    model = Meseros
    template_name = 'eliminar_mesero.html'
    success_url = reverse_lazy('meseros_list')

class TuVistaProtegida(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"mensaje": "Esta vista está protegida por JWT."})

@api_view(['GET'])
def tu_vista_sin_proteccion(request):
    return Response({'mensaje': 'Esta es una vista sin protección.'})

@api_view(['POST'])
def crear_mesero(request):
    if request.method == 'POST':
        serializer = MeseroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditarMeseroView(generics.UpdateAPIView):
    queryset = Meseros.objects.all()
    serializer_class = MeseroSerializer
    permission_classes = [permissions.IsAuthenticated]

class DetalleMeseroView(generics.RetrieveAPIView):
    queryset = Meseros.objects.all()
    serializer_class = MeseroSerializer
    permission_classes = [permissions.IsAuthenticated]

class EliminarMeseroView(generics.DestroyAPIView):
    queryset = Meseros.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
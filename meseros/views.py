from django.shortcuts import render
from .models import Meseros

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

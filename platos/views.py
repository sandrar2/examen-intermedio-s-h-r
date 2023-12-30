from django.shortcuts import render
from .models import Platos

def platos_list(request):
    data_context = {
        'nombre': 'Ceviche',
        'precio': 25,
        'procedencia': 'Peru',
    }

    return render(request, 'platos_list.html', context=data_context)

def platillos_peru_mayor_40(request):
    platillos_peru_mayor_40 = Platos.objects.filter(procedencia='Perú', precio__gt=40)[:3]

    data_context = {
        'platillos_peru_mayor_40': platillos_peru_mayor_40
    }

    return render(request, 'platillos_peru_mayor_40.html', context=data_context)


def eliminar_platos_menor_15(request):
    Platos.objects.filter(precio__lt=15).delete()

    data_context = {
        'mensaje': 'Platos con precio menor a 15 soles eliminados correctamente.'
    }

    return render(request, 'eliminar_platos_menor_15.html', context=data_context)

def platos_mayores_de_50(request):
    platos_mayores = Platos.objects.filter(precio__gt=50)
    return render(request, 'platos_mayores_de_50.html', {'platos_mayores': platos_mayores})


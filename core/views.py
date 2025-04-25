from django.shortcuts import render
from .models import ItemCuadricula


def index(request):
    # Filtramos los items por sección
    fundacion_items = ItemCuadricula.objects.filter(seccion='fundacion')
    instituto_items = ItemCuadricula.objects.filter(seccion='instituto')
    lutheria_items = ItemCuadricula.objects.filter(seccion='lutheria')

    # Pasamos los datos al template
    return render(request, 'core/index.html', {
        'fundacion_items': fundacion_items,
        'instituto_items': instituto_items,
        'lutheria_items': lutheria_items,
    })

def cuadricula(request, seccion):
    items = ItemCuadricula.objects.filter(seccion=seccion)
    return render(request, 'core/cuadricula.html', {'items': items, 'seccion': seccion})

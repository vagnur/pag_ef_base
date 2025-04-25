from django.shortcuts import render
from .models import ItemCuadricula
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import EntryForm
from django.contrib import messages  


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

@login_required
def create_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            # Crear la entrada sin guardar todavía
            entry = form.save(commit=False)
            entry.created_by = request.user  # Asociar la entrada al usuario logueado
            
            # Asegurarnos de que 'nombre' se esté guardando
            entry.nombre = form.cleaned_data['nombre']  # Asignar el valor de 'nombre' manualmente
            entry.save()  # Guardamos la entrada

            # Mensaje de éxito
            section_name = dict(ItemCuadricula.SECCIONES).get(entry.seccion)
            messages.success(request, f'¡La entrada para {section_name} ha sido creada con éxito!')

            # Crear un nuevo formulario vacío para limpiar los campos
            form = EntryForm()  # Reinicia el formulario (lo limpia)

            # Renderizamos la página con el formulario vacío
            return render(request, 'create_entry.html', {'form': form})

    else:
        form = EntryForm()

    return render(request, 'create_entry.html', {'form': form})







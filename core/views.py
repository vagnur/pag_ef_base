from django.shortcuts import render
from .models import ItemCuadricula
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages  
from .forms import ItemCuadriculaForm
import os


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
def admin_panel_home(request):
    return render(request, 'admin_panel/home.html')

@login_required
def admin_panel_items(request):
    return render(request, 'admin_panel/items_list.html')

@login_required
def admin_panel_items(request):
    seccion_filtrada = request.GET.get('seccion', None)

    if seccion_filtrada:
        items = ItemCuadricula.objects.filter(seccion=seccion_filtrada).order_by('nombre')
    else:
        items = ItemCuadricula.objects.all().order_by('seccion', 'nombre')

    # SECCIONES CORRECTAS
    secciones = ['fundacion', 'instituto', 'lutheria']

    return render(request, 'admin_panel/items_list.html', {
        'items': items,
        'secciones': secciones,
        'seccion_filtrada': seccion_filtrada,
    })

@login_required
def admin_panel_create_item(request):
    if request.method == 'POST':
        form = ItemCuadriculaForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            messages.success(request, 'Entrada creada exitosamente.')
            return redirect('admin_panel_items_by_section', seccion=item.seccion)

    else:
        form = ItemCuadriculaForm()

    return render(request, 'admin_panel/item_form.html', {'form': form, 'accion': 'Crear Nueva Entrada'})

@login_required
def admin_panel_edit_item(request, item_id):
    item = ItemCuadricula.objects.get(id=item_id)

    if request.method == 'POST':
        old_image = item.imagen  # Guardamos la imagen antigua

        form = ItemCuadriculaForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            new_image = form.cleaned_data.get('imagen')

            # Si subieron una imagen nueva distinta
            if new_image and old_image != new_image:
                # Eliminar la imagen anterior
                if old_image and os.path.isfile(old_image.path):
                    os.remove(old_image.path)

            item = form.save()

            messages.success(request, 'Entrada editada exitosamente.')
            return redirect('admin_panel_items_by_section', seccion=item.seccion)
    else:
        form = ItemCuadriculaForm(instance=item)

    return render(request, 'admin_panel/item_form.html', {'form': form, 'accion': 'Editar Entrada'})


@login_required
def admin_panel_items_by_section(request, seccion):
    seccion = seccion.lower()  # Aseguramos que esté en minúsculas
    secciones_validas = {
        'fundacion': 'Fundación',
        'instituto': 'Instituto',
        'lutheria': 'Luthería',
    }

    if seccion not in secciones_validas:
        return redirect('admin_panel_home')  # O a donde prefieras si sección inválida

    items = ItemCuadricula.objects.filter(seccion=seccion).order_by('nombre')
    nombre_seccion = secciones_validas[seccion]

    return render(request, 'admin_panel/items_list.html', {
    'items': items,
    'nombre_seccion': nombre_seccion,
    'seccion_actual': seccion,  # <<<< PASAMOS ESTO
    })

import os

@login_required
def admin_panel_delete_item(request, item_id, seccion):
    item = ItemCuadricula.objects.get(id=item_id)

    if request.method == 'POST':
        # Eliminar archivo de imagen si existe
        if item.imagen and os.path.isfile(item.imagen.path):
            os.remove(item.imagen.path)
        
        # Luego eliminar el objeto
        item.delete()

        messages.success(request, 'Entrada eliminada exitosamente.')
        return redirect('admin_panel_items_by_section', seccion=seccion)

    return redirect('admin_panel_home')  # Si alguien intenta hacer GET raro


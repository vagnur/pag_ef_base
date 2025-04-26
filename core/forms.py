from django import forms
from .models import ItemCuadricula

class ItemCuadriculaForm(forms.ModelForm):
    class Meta:
        model = ItemCuadricula
        fields = ['seccion', 'nombre', 'imagen', 'resumen', 'descripcion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
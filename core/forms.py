from django import forms
from .models import ItemCuadricula

class EntryForm(forms.ModelForm):
    class Meta:
        model = ItemCuadricula
        fields = ['nombre', 'seccion', 'imagen', 'resumen', 'descripcion']

    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}), required=True)
    imagen = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), required=True)
    seccion = forms.ChoiceField(choices=ItemCuadricula.SECCIONES, widget=forms.RadioSelect, required=True)
    resumen = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Resumen corto'}), required=True)
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción larga', 'rows': 4}),
        required=True
    )

from django.db import models
import os
from uuid import uuid4

def image_upload_path(instance, filename):
    """
    Genera una ruta dinámica para guardar imágenes basada en la sección del item.
    """
    ext = filename.split('.')[-1]  # Extraemos la extensión del archivo
    filename = f"{uuid4().hex}.{ext}"  # Generamos un nombre único para evitar colisiones
    return os.path.join(f'cuadricula_images/{instance.seccion}/', filename)

class ItemCuadricula(models.Model):
    SECCIONES = [
        ('fundacion', 'Fundación'),
        ('instituto', 'Instituto'),
        ('lutheria', 'Luthería'),
    ]
    
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to=image_upload_path)
    resumen = models.CharField(max_length=150)  # Texto corto para la cuadrícula
    descripcion = models.TextField()  # Usar un TextField normal
    seccion = models.CharField(max_length=10, choices=SECCIONES)
    
    def __str__(self):
        return f"{self.nombre} - {self.seccion}"

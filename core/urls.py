from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from core import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create-entry/', views.create_entry, name='create_entry'),  # URL para crear entradas
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from core import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin-panel/', views.admin_panel_home, name='admin_panel_home'),
    path('admin-panel/items/', views.admin_panel_items, name='admin_panel_items'),
    path('admin-panel/items/create/', views.admin_panel_create_item, name='admin_panel_create_item'),
    path('admin-panel/items/<int:item_id>/edit/', views.admin_panel_edit_item, name='admin_panel_edit_item'),
    path('admin-panel/<str:seccion>/', views.admin_panel_items_by_section, name='admin_panel_items_by_section'),
    path('admin-panel/items/<int:item_id>/delete/', views.admin_panel_delete_item, name='admin_panel_delete_item'),
    path('admin-panel/items/<int:item_id>/delete/<str:seccion>/', views.admin_panel_delete_item, name='admin_panel_delete_item'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

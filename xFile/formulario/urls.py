from django.urls import path
from . import views, view_export, view_gen_contratos
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views

# app_name = '_monedas'
# Crear un router para las vistas
router = DefaultRouter()

urlpatterns = [
    # URLs para Formulario
    path('', views.DatosListView.as_view(), name='datos_list'),
    path('crear/', views.DatosCreateView.as_view(), name='dato_create'),
    path('<str:pk>/editar/', views.DatosUpdateView.as_view(), name='dato_update'),
    path('<str:pk>/eliminar/', views.datos_delete, name='datos_delete'),

]
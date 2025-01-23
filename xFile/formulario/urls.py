from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

# app_name = '_monedas'
# Crear un router para las vistas
router = DefaultRouter()

urlpatterns = [
    # URLs para Moneda
    path('', views.MonedaListView.as_view(), name='datos_list'),
    path('crear/', views.MonedaCreateView.as_view(), name='dato_create'),
    path('<str:pk>/editar/', views.MonedaUpdateView.as_view(), name='dato_update'),
    path('<str:pk>/eliminar/', views.MonedaDelete, name='dato_delete'),
]
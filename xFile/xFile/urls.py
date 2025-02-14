"""
URL configuration for xFile project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from usuario.views import home, LoginView, RegisterView, SignOutView
from django.conf import settings
from django.conf.urls.static import static

from formulario.views import (get_municipios, get_parroquias, get_sector,
                              ambiente_create, ambiente_delete, AmbienteListView, ambiente_update,
                              LinderoListView, lindero_create, lindero_delete, lindero_update,
                              EstadoListView, estado_create, estado_delete, estado_update,
                              MunicipioListView, municipio_create, municipio_delete, municipio_update,
                              ParroquiaListView, parroquia_create, parroquia_delete, parroquia_update,
                              SectorListView, sector_create, sector_delete, sector_update,
                              EntidadesListView, entidades_create, EntidadesDetailView, entidades_update, entidades_delete,
                              RepresentantesListView, representantes_create, RepresentantesDetailView, representantes_update, representantes_delete
                              )
from formulario.view_export import exportar_datos_xlsx
from formulario.view_gen_contratos import genContratosTotales, genContratosUnico

urlpatterns = [
    path('', home, name='home'),
    
    # path('api/urbanismos/', get_urbanismo, name='obtener_urbanismo_por_sector'),
    path('api/sector/', get_sector, name='obtener_sector_por_parroquias'), # /api/sector/?parroquia=1
    path('api/parroquias/', get_parroquias, name='obtener_parroquias_por_municipio'), # /api/parroquias/?municipio=VAR
    path('api/municipios/', get_municipios, name='obtener_municipios_por_estado'), # /api/municipios/?estado=LGR
    
    path('admin/', admin.site.urls),
    
    path('formulario/', include('formulario.urls')),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('logout', SignOutView.as_view(), name='logout'),
    
    
    # URLs para Ambiente
    path('ambientes/', AmbienteListView.as_view(), name='ambiente_list'),
    path('ambientes/crear/', ambiente_create, name='ambiente_create'),
    path('ambientes/<str:pk>/editar/', ambiente_update, name='ambiente_update'),
    path('ambientes/<str:pk>/eliminar/', ambiente_delete, name='ambiente_delete'),
    
    # URLs para Lindero
    path('linderos/', LinderoListView.as_view(), name='lindero_list'),
    path('linderos/crear/', lindero_create, name='lindero_create'),
    path('linderos/<str:pk>/editar/', lindero_update, name='lindero_update'),
    path('linderos/<str:pk>/eliminar/', lindero_delete, name='lindero_delete'),
    
    # URLs para Estado
    path('estados/', EstadoListView.as_view(), name='estado_list'),
    path('estados/crear/', estado_create, name='estado_create'),
    path('estados/<str:pk>/editar/', estado_update, name='estado_update'),
    path('estados/<str:pk>/eliminar/', estado_delete, name='estado_delete'),
    
    # URLs para Municipio
    path('municipios/', MunicipioListView.as_view(), name='municipio_list'),
    path('municipios/crear/', municipio_create, name='municipio_create'),
    path('municipios/<str:pk>/editar/', municipio_update, name='municipio_update'),
    path('municipios/<str:pk>/eliminar/', municipio_delete, name='municipio_delete'),
    
    # URLs para Parroquia
    path('parroquias/', ParroquiaListView.as_view(), name='parroquia_list'),
    path('parroquias/crear/', parroquia_create, name='parroquia_create'),
    path('parroquias/<str:pk>/editar/', parroquia_update, name='parroquia_update'),
    path('parroquias/<str:pk>/eliminar/', parroquia_delete, name='municipio_delete'),
    
    # URLs para Sector
    path('sectores/', SectorListView.as_view(), name='sector_list'),
    path('sectores/crear/', sector_create, name='sector_create'),
    path('sectores/<str:pk>/editar/', sector_update, name='sector_update'),
    path('sectores/<str:pk>/eliminar/', sector_delete, name='municipio_delete'),
    
    # URLs para Entidades
    path('entidades/', EntidadesListView.as_view(), name='entidades_list'),
    path('entidades/crear/', entidades_create, name='entidades_create'),
    path('entidades/<int:pk>/', EntidadesDetailView.as_view(), name='entidades_detail'),
    path('entidades/<int:pk>/editar/', entidades_update, name='entidades_update'),
    path('entidades/<int:pk>/eliminar/', entidades_delete, name='entidades_delete'),
    
    # URLs para Representantes
    path('representantes/', RepresentantesListView.as_view(), name='representantes_list'),
    path('representantes/crear/', representantes_create, name='representantes_create'),
    path('representantes/<str:pk>/', RepresentantesDetailView.as_view(), name='representantes_detail'),
    path('representantes/<str:pk>/editar/', representantes_update, name='representantes_update'),
    path('representantes/<str:pk>/eliminar/', representantes_delete, name='representantes_delete'),
    
    path('exportar/', exportar_datos_xlsx, name='exportar_xlsx'),
    path('generar-contatos/', genContratosTotales, name='genContratosTotales'),
    path('generar-contatos/<str:pk>', genContratosUnico, name='genContratosUnico')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

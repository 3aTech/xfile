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
from usuario.views import home, LoginView, RegisterView, SignOutView

from formulario.views import ambiente_create, ambiente_delete, AmbienteListView, ambiente_update, lindero_create, lindero_delete, LinderoListView, lindero_update
urlpatterns = [
    path('', home, name='home'),
    
    path('admin/', admin.site.urls),
    
    path('formulario/', include('formulario.urls')),
    
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('logout', SignOutView.as_view(), name='logout'),
    
    # URLs para Ambiente
    path('ambientes/', AmbienteListView.as_view(), name='ambiente_list'),
    path('ambientes/crear/', ambiente_create, name='ambiente_create'),
    path('ambientes/<int:pk>/editar/', ambiente_update, name='ambiente_update'),
    path('ambientes/<int:pk>/eliminar/', ambiente_delete, name='ambiente_delete'),
    
    # URLs para Lindero
    path('linderos/', LinderoListView.as_view(), name='lindero_list'),
    path('linderos/crear/', lindero_create, name='lindero_create'),
    path('linderos/<int:pk>/editar/', lindero_update, name='lindero_update'),
    path('linderos/<int:pk>/eliminar/', lindero_delete, name='lindero_delete'),
]

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Datos
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import DatosSerializer
from rest_framework import status

# Create your views here.

# Vista para listar los datos
class DatosListView(LoginRequiredMixin, ListView):
    model = Datos
    template_name = 'frmRegistro.html'
    context_object_name = 'Registros'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(cedula__icontains=search)
        return queryset.order_by('cedula')

class DatosCreateView(LoginRequiredMixin, CreateView):
    model = Datos
    template_name = 'frmRegistro.html'
    fields = [
        'serial_cliente', 'sello_dorado', 'cedula', 'nombre1', 'nombre2', 'apellido1', 'apellido2',
        'torre', 'piso', 'apartamento', 'monto_credito', 'precio_venta', 'precio_venta_divisa',
        'inicial', 'inicial_porcentaje', 'identificador', 'denominara', 'ciudadano_ciudadana',
        'anios', 'meses', 'cuota_mensual', 'cuota_mensual_divisa', 'flat', 'flat_divisa',
        'cuota_financiera', 'cuota_financiera_divisa', 'fongar', 'fongar_divisa', 'expediente',
        'contrato_nro', 'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo'
    ]
    success_url = reverse_lazy('datos_list')
    
    def form_valid(self, form):
        form.instance.us_in = self.request.user.username
        messages.success(self.request, 'Datos creado exitosamente.')
        return super().form_valid(form)


class DatosUpdateView(LoginRequiredMixin, UpdateView):
    model = Datos
    template_name = 'frmRegistro.html'
    fields = [
        'sello_dorado', 'cedula', 'nombre1', 'nombre2', 'apellido1', 'apellido2',
        'torre', 'piso', 'apartamento', 'monto_credito', 'precio_venta', 'precio_venta_divisa',
        'inicial', 'inicial_porcentaje', 'identificador', 'denominara', 'ciudadano_ciudadana',
        'anios', 'meses', 'cuota_mensual', 'cuota_mensual_divisa', 'flat', 'flat_divisa',
        'cuota_financiera', 'cuota_financiera_divisa', 'fongar', 'fongar_divisa', 'expediente',
        'contrato_nro', 'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo'
    ]
    success_url = reverse_lazy('datos_list')
    
    def form_valid(self, form):
        form.instance.us_mo = self.request.user.username
        messages.success(self.request, 'País actualizado exitosamente.')
        return super().form_valid(form)

class DatosDeleteView(LoginRequiredMixin, DeleteView):
    model = Datos
    template_name = 'ubicacion/del_pais.html'
    success_url = reverse_lazy('datos_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'País eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)
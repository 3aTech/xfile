from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Datos, Ambiente, Lindero
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import DatosSerializer, AmbienteSerializer, LinderoSerializer
from rest_framework import status

# Create your views here.

# Vista para listar los datos
class DatosListView(LoginRequiredMixin, ListView):
    model = Datos
    template_name = 'pages/list_datos.html'
    context_object_name = 'registros'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(cedula__icontains=search)
        return queryset.order_by('cedula')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_registros'] = self.get_queryset().count()  # Agregar la cantidad de registros
        return context

class DatosCreateView(LoginRequiredMixin, CreateView):
    model = Datos
    template_name = 'pages/frmDatos.html'
    fields = [
        'serial_cliente', 'sello_dorado', 'cedula', 'nombre1', 'nombre2', 'apellido1', 'apellido2',
        'urbanismo', 'torre', 'piso', 'apartamento', 'monto_credito', 'precio_venta', 'precio_venta_divisa',
        'inicial', 'inicial_porcentaje', 'identificador', 'denominara', 'ciudadano_ciudadana',
        'anios', 'meses', 'cuota_mensual', 'cuota_mensual_divisa', 'flat', 'flat_divisa',
        'cuota_financiera', 'cuota_financiera_divisa', 'fongar', 'fongar_divisa', 'expediente',
        'contrato_nro'
    ]
    success_url = reverse_lazy('datos_list')
    
    def form_valid(self, form):
        print(form.instance)
        form.instance.us_in = self.request.user.username
        messages.success(self.request, 'Datos creado exitosamente.')
        print(form.instance)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        for field, error in form.errors.items():
            messages.error(self.request, f"{field}: {error}")
        return super().form_invalid(form)


class DatosUpdateView(LoginRequiredMixin, UpdateView):
    model = Datos
    template_name = 'pages/frmDatos.html'
    fields = [
        'sello_dorado', 'cedula', 'nombre1', 'nombre2', 'apellido1', 'apellido2',
        'urbanismo', 'torre', 'piso', 'apartamento', 'monto_credito', 'precio_venta', 'precio_venta_divisa',
        'inicial', 'inicial_porcentaje', 'identificador', 'denominara', 'ciudadano_ciudadana',
        'anios', 'meses', 'cuota_mensual', 'cuota_mensual_divisa', 'flat', 'flat_divisa',
        'cuota_financiera', 'cuota_financiera_divisa', 'fongar', 'fongar_divisa', 'expediente',
        'contrato_nro'
    ]
    success_url = reverse_lazy('datos_list')
    
    def form_valid(self, form):
        form.instance.us_mo = self.request.user.username
        messages.success(self.request, 'Datos actualizado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, error in form.errors.items():
            messages.error(self.request, f"{field}: {error}")
            print( messages.error(self.request, f"{field}: {error}"))
        return super().form_invalid(form)

class DatosDeleteView(LoginRequiredMixin, DeleteView):
    model = Datos
    template_name = 'ubicacion/del_pais.html'
    success_url = reverse_lazy('datos_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Datos eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

# Vista para listar y gestionar ambientes
class AmbienteListView(LoginRequiredMixin, ListView):
    model = Ambiente
    template_name = 'pages/ambientes.html'  # Cambiar a la nueva plantilla
    context_object_name = 'registros'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(ambiente__icontains=search)
        return queryset.order_by('ambiente')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_registros'] = self.get_queryset().count()  # Agregar la cantidad de registros
        return context

# Vista para crear un nuevo ambiente
class AmbienteCreateView(LoginRequiredMixin, CreateView):
    model = Ambiente
    fields = ['ambiente']
    success_url = reverse_lazy('ambiente_list')

    def form_valid(self, form):
        form.instance.us_in = self.request.user.username
        messages.success(self.request, 'Ambiente creado exitosamente.')
        return super().form_valid(form)

# Vista para actualizar un ambiente existente
class AmbienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Ambiente
    fields = ['ambiente']
    success_url = reverse_lazy('ambiente_list')

    def form_valid(self, form):
        form.instance.us_mo = self.request.user.username
        messages.success(self.request, 'Ambiente actualizado exitosamente.')
        return super().form_valid(form)

# Vista para eliminar un ambiente
class AmbienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Ambiente
    success_url = reverse_lazy('ambiente_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Ambiente eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

# Vista para manejar las solicitudes AJAX para crear, editar y eliminar
@api_view(['POST'])
def ambiente_create(request):
    serializer = AmbienteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(us_in=request.user.username)
        return Response({'message': 'Ambiente creado exitosamente.'}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def ambiente_update(request, pk):
    ambiente = Ambiente.objects.get(pk=pk)
    serializer = AmbienteSerializer(ambiente, data=request.data)
    if serializer.is_valid():
        serializer.save(us_mo=request.user.username)
        return Response({'message': 'Ambiente actualizado exitosamente.'}, status=200)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def ambiente_delete(request, pk):
    ambiente = Ambiente.objects.get(pk=pk)
    ambiente.delete()
    return Response({'message': 'Ambiente eliminado exitosamente.'}, status=204)

# Vista para listar y gestionar linderos
class LinderoListView(LoginRequiredMixin, ListView):
    model = Lindero
    template_name = 'pages/linderos.html'  # Cambiar a la nueva plantilla
    context_object_name = 'registros'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(lindero__icontains=search)
        return queryset.order_by('lindero')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_registros'] = self.get_queryset().count()  # Agregar la cantidad de registros
        return context

# Vista para crear un nuevo ambiente
class LinderoCreateView(LoginRequiredMixin, CreateView):
    model = Lindero
    fields = ['lindero']
    success_url = reverse_lazy('lindero_list')

    def form_valid(self, form):
        form.instance.us_in = self.request.user.username
        messages.success(self.request, 'Lindero creado exitosamente.')
        return super().form_valid(form)

# Vista para actualizar un lindero existente
class LinderoUpdateView(LoginRequiredMixin, UpdateView):
    model = Lindero
    fields = ['lindero']
    success_url = reverse_lazy('lindero_list')

    def form_valid(self, form):
        form.instance.us_mo = self.request.user.username
        messages.success(self.request, 'Lindero actualizado exitosamente.')
        return super().form_valid(form)

# Vista para eliminar un lindero
class LinderoDeleteView(LoginRequiredMixin, DeleteView):
    model = Lindero
    success_url = reverse_lazy('lindero_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Lindero eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

# Vista para manejar las solicitudes AJAX para crear, editar y eliminar
@api_view(['POST'])
def lindero_create(request):
    serializer = LinderoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(us_in=request.user.username)
        return Response({'message': 'Lindero creado exitosamente.'}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def lindero_update(request, pk):
    lindero = Lindero.objects.get(pk=pk)
    serializer = LinderoSerializer(lindero, data=request.data)
    if serializer.is_valid():
        serializer.save(us_mo=request.user.username)
        return Response({'message': 'Lindero actualizado exitosamente.'}, status=200)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def lindero_delete(request, pk):
    lindero = Lindero.objects.get(pk=pk)
    lindero.delete()
    return Response({'message': 'Lindero eliminado exitosamente.'}, status=204)
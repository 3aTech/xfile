from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import (Datos, Ambientes, Linderos, Representantes, 
                     Estados, Municipios, Parroquias, Sectores, Entidades)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import (DatosSerializer, 
                          AmbienteSerializer, LinderoSerializer,
                          EstadoSerializer, MunicipioSerializer, ParroquiaSerializer, SectorSerializer,
                          EntidadesSerializer, RepresentanteSerializer)
from rest_framework import status

# Vista para obtener sector según la parroquia
@api_view(['GET'])
def get_sector(request):
    parroquia_id = request.GET.get('parroquia')
    if not parroquia_id:
        return Response({"error": "La parroquia es requerida."}, status=status.HTTP_400_BAD_REQUEST)
    sectores = Sectores.objects.filter(parroquia=parroquia_id)
    serializer = SectorSerializer(sectores, many=True)
    return Response(serializer.data)

# Vista para obtener parroquias según el municipio
@api_view(['GET'])
def get_parroquias(request):
    municipio_id = request.GET.get('municipio')
    if not municipio_id:
        return Response({"error": "El municipio es requerido."}, status=status.HTTP_400_BAD_REQUEST)
    parroquias = Parroquias.objects.filter(municipio__co_municipio=municipio_id)
    serializer = ParroquiaSerializer(parroquias, many=True)
    return Response(serializer.data)

# Vista para obtener municipios según el estado
@api_view(['GET'])
def get_municipios(request):
    estado_id = request.GET.get('estado')
    if not estado_id:
        return Response({"error": "El estado es requerido."}, status=status.HTTP_400_BAD_REQUEST)
    municipios = Municipios.objects.filter(estado__co_estado=estado_id)
    serializer = MunicipioSerializer(municipios, many=True)
    return Response(serializer.data)

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
        context['representantes'] = Representantes.objects.all()
        context['estados'] = Estados.objects.all()
        context['municipios'] = Municipios.objects.all()
        context['parroquias'] = Parroquias.objects.all()
        context['sectores'] = Sectores.objects.all()
        context['total_registros'] = self.get_queryset().count()  # Agregar la cantidad de registros
        return context

class DatosCreateView(LoginRequiredMixin, CreateView):
    model = Datos
    template_name = 'pages/frmDatos.html'
    fields = [
        'serial_cliente', 'expediente', 'contrato_nro', 'representante', 'sello_dorado', 'nro_dorado_oficio',  
        'cedula', 'identificador', 'denominara', 'ciudadano_ciudadana', 'nombre1', 'nombre2', 'apellido1', 'apellido2',
        'estado', 'municipio', 'parroquia', 'sector', 'urbanismo', 'torre', 'piso', 'apartamento', 'metros_cuadrados',
        'lindero_norte', 'lindero_sur', 'lindero_este', 'lindero_oeste', 'ambientes',
        'monto_credito', 'precio_venta', 'precio_venta_divisa', 'inicial', 'inicial_divisa', 'inicial_porcentaje',  
        'anios', 'meses', 'cuota_mensual', 'cuota_mensual_divisa', 'flat', 'flat_divisa',
        'cuota_financiera', 'cuota_financiera_divisa', 'fongar', 'fongar_divisa'
        
    ]
    success_url = reverse_lazy('datos_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['representantes'] = Representantes.objects.all()
        context['estados'] = Estados.objects.all()
        context['municipios'] = Municipios.objects.all()
        context['parroquias'] = Parroquias.objects.all()
        context['sectores'] = Sectores.objects.all()
        
        return context
    
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
        'serial_cliente', 'expediente', 'contrato_nro', 'representante', 'sello_dorado', 
        'nro_dorado_oficio', 'cedula', 'identificador', 'denominara', 'ciudadano_ciudadana', 
        'nombre1', 'nombre2', 'apellido1', 'apellido2', 'estado', 'municipio', 'parroquia', 
        'sector', 'urbanismo', 'torre', 'piso', 'apartamento', 'metros_cuadrados', 
        'lindero_norte', 'lindero_sur', 'lindero_este', 'lindero_oeste', 'ambientes',
        'monto_credito', 'precio_venta', 'precio_venta_divisa', 'inicial', 'inicial_divisa', 'inicial_porcentaje',  
        'anios', 'meses', 'cuota_mensual', 'cuota_mensual_divisa', 'flat', 'flat_divisa',
        'cuota_financiera', 'cuota_financiera_divisa', 'fongar', 'fongar_divisa'
    ]
    success_url = reverse_lazy('datos_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['representantes'] = Representantes.objects.all()
        context['estados'] = Estados.objects.all()
        context['municipios'] = Municipios.objects.all()
        context['parroquias'] = Parroquias.objects.all()
        context['sectores'] = Sectores.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.us_mo = self.request.user.username
        messages.success(self.request, 'Datos actualizado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, error in form.errors.items():
            messages.error(self.request, f"{field}: {error}")
        return super().form_invalid(form)
 
@api_view(['DELETE'])
def datos_delete(request, pk):
    try:
        dato = Datos.objects.get(pk=pk)
        dato.delete()
        return Response({'message': 'Registro eliminado exitosamente.'}, status=204)
    except Datos.DoesNotExist:
        return Response({'error': 'Registro no encontrado.'}, status=404)

# Vista para listar y gestionar ambientes
class AmbienteListView(LoginRequiredMixin, ListView):
    model = Ambientes
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
    model = Ambientes
    fields = ['ambiente']
    success_url = reverse_lazy('ambiente_list')

    def form_valid(self, form):
        form.instance.us_in = self.request.user.username
        messages.success(self.request, 'Ambiente creado exitosamente.')
        return super().form_valid(form)

# Vista para actualizar un ambiente existente
class AmbienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Ambientes
    fields = ['ambiente']
    success_url = reverse_lazy('ambiente_list')

    def form_valid(self, form):
        form.instance.us_mo = self.request.user.username
        messages.success(self.request, 'Ambiente actualizado exitosamente.')
        return super().form_valid(form)

# Vista para eliminar un ambiente
class AmbienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Ambientes
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
    ambiente = Ambientes.objects.get(pk=pk)
    serializer = AmbienteSerializer(ambiente, data=request.data)
    if serializer.is_valid():
        serializer.save(us_mo=request.user.username)
        return Response({'message': 'Ambiente actualizado exitosamente.'}, status=200)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def ambiente_delete(request, pk):
    ambiente = Ambientes.objects.get(pk=pk)
    ambiente.delete()
    return Response({'message': 'Ambiente eliminado exitosamente.'}, status=204)

# Vista para listar y gestionar linderos
class LinderoListView(LoginRequiredMixin, ListView):
    model = Linderos
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
    model = Linderos
    fields = ['lindero']
    success_url = reverse_lazy('lindero_list')

    def form_valid(self, form):
        form.instance.us_in = self.request.user.username
        messages.success(self.request, 'Lindero creado exitosamente.')
        return super().form_valid(form)

# Vista para actualizar un lindero existente
class LinderoUpdateView(LoginRequiredMixin, UpdateView):
    model = Linderos
    fields = ['lindero']
    success_url = reverse_lazy('lindero_list')

    def form_valid(self, form):
        form.instance.us_mo = self.request.user.username
        messages.success(self.request, 'Lindero actualizado exitosamente.')
        return super().form_valid(form)

# Vista para eliminar un lindero
class LinderoDeleteView(LoginRequiredMixin, DeleteView):
    model = Linderos
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
    lindero = Linderos.objects.get(pk=pk)
    serializer = LinderoSerializer(lindero, data=request.data)
    if serializer.is_valid():
        serializer.save(us_mo=request.user.username)
        return Response({'message': 'Lindero actualizado exitosamente.'}, status=200)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def lindero_delete(request, pk):
    lindero = Linderos.objects.get(pk=pk)
    lindero.delete()
    return Response({'message': 'Lindero eliminado exitosamente.'}, status=204)

# Vistas para Estado
class EstadoListView(LoginRequiredMixin, ListView):
    model = Estados
    template_name = 'pages/estados.html'
    context_object_name = 'registros'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(des_estado__icontains=search)
        return queryset.order_by('des_estado')

# Vista para manejar las solicitudes AJAX para crear, editar y eliminar
@api_view(['POST'])
def estado_create(request):
    serializer = EstadoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(us_in=request.user.username)
        return Response({'message': 'Estado creado exitosamente.'}, status=201)
    else:
        for field, error in serializer.errors.items():
            messages.error(request, f"{field}: {error}")  # Enviar mensaje de error
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def estado_update(request, pk):
    estado = Estados.objects.get(pk=pk)
    serializer = EstadoSerializer(estado, data=request.data)
    if serializer.is_valid():
        serializer.save(us_mo=request.user.username)
        return Response({'message': 'Estado actualizado exitosamente.'}, status=200)
    else:
        for field, error in serializer.errors.items():
            messages.error(request, f"{field}: {error}")  # Enviar mensaje de error
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def estado_delete(request, pk):
    estado = Estados.objects.get(pk=pk)
    estado.delete()
    return Response({'message': 'Estado eliminado exitosamente.'}, status=204)


# Vistas para Municipio
class MunicipioListView(LoginRequiredMixin, ListView):
    model = Municipios
    template_name = 'pages/municipios.html'
    context_object_name = 'registros'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        estado = self.request.GET.get('estado', '')
        
        if search:
            queryset = queryset.filter(des_municipio__icontains=search)
        if estado:
            queryset = queryset.filter(estado__co_estado=estado)

        return queryset.select_related('estado').order_by('des_municipio')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estados'] = Estados.objects.all()  # Agregar la lista de estados
        return context

# Vista para manejar las solicitudes AJAX para crear, editar y eliminar
@api_view(['POST'])
def municipio_create(request):
    serializer = MunicipioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(us_in=request.user.username)
        return Response({'message': 'Municipio creado exitosamente.'}, status=201)
    else:
        for field, error in serializer.errors.items():
            messages.error(request, f"{field}: {error}")  # Enviar mensaje de error
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def municipio_update(request, pk):
    try:
        municipio = Municipios.objects.get(co_municipio=pk)
        estado = Estados.objects.get(co_estado=request.data.get('estado'))
        
        serializer = MunicipioSerializer(municipio, data={
            'co_municipio': request.data.get('co_municipio'),
            'des_municipio': request.data.get('des_municipio'),
            'estado': estado.co_estado
        })
        
        if serializer.is_valid():
            serializer.save(us_mo=request.user.username)
            return Response({'message': 'Municipio actualizado exitosamente.'}, status=200)
        else:
            return Response(serializer.errors, status=400)
    except Municipios.DoesNotExist:
        return Response({'error': 'Municipio no encontrado.'}, status=404)
    except Estados.DoesNotExist:
        return Response({'error': 'Estado no encontrado.'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['DELETE'])
def municipio_delete(request, pk):
    municipio = Municipios.objects.get(pk=pk)
    municipio.delete()
    return Response({'message': 'Municipio eliminado exitosamente.'}, status=204)

# Vistas para Parroquia
class ParroquiaListView(LoginRequiredMixin, ListView):
    model = Parroquias
    template_name = 'pages/parroquias.html'
    context_object_name = 'registros'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        municipio = self.request.GET.get('municipio', '')
        
        if search:
            queryset = queryset.filter(des_parroquia__icontains=search)
        if municipio:
            queryset = queryset.filter(municipio__co_municipio=municipio)

        return queryset.select_related('municipio').order_by('des_parroquia')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['municipios'] = Municipios.objects.all()  # Agregar la lista de municipio
        return context

# Vista para manejar las solicitudes AJAX para crear, editar y eliminar
@api_view(['POST'])
def parroquia_create(request):
    serializer = ParroquiaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(us_in=request.user.username)
        return Response({'message': 'Parroquia creado exitosamente.'}, status=201)
    else:
        for field, error in serializer.errors.items():
            messages.error(request, f"{field}: {error}")  # Enviar mensaje de error
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def parroquia_update(request, pk):
    try:
        parroquia = Parroquias.objects.get(co_parroquia=pk)
        municipio = Municipios.objects.get(co_municipio=request.data.get('municipio'))
        
        serializer = ParroquiaSerializer(parroquia, data={
            'co_parroquia': request.data.get('co_parroquia'),
            'des_parroquia': request.data.get('des_parroquia'),
            'municipio': municipio.co_municipio
        })
        
        if serializer.is_valid():
            serializer.save(us_mo=request.user.username)
            return Response({'message': 'Parroquia actualizada exitosamente.'}, status=200)
        else:
            return Response(serializer.errors, status=400)
    except Parroquias.DoesNotExist:
        return Response({'error': 'Parroquia no encontrada.'}, status=404)
    except Municipios.DoesNotExist:
        return Response({'error': 'Parroquia no encontrada.'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['DELETE'])
def parroquia_delete(request, pk):
    parroquia = Parroquias.objects.get(pk=pk)
    parroquia.delete()
    return Response({'message': 'Parroquia eliminado exitosamente.'}, status=204)

# Vistas para Sector
class SectorListView(LoginRequiredMixin, ListView):
    model = Sectores
    template_name = 'pages/sectores.html'
    context_object_name = 'registros'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        parroquia = self.request.GET.get('parroquia', '')
        
        if search:
            queryset = queryset.filter(des_sector__icontains=search)
        if parroquia:
            queryset = queryset.filter(parroquia__co_parroquia=parroquia)

        return queryset.select_related('parroquia').order_by('des_sector')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parroquias'] = Parroquias.objects.all()  # Asegúrate de que esto esté presente
        return context

# Vista para manejar las solicitudes AJAX para crear, editar y eliminar
@api_view(['POST'])
def sector_create(request):
    serializer = SectorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(us_in=request.user.username)
        return Response({'message': 'Sector creada exitosamente.'}, status=201)
    else:
        for field, error in serializer.errors.items():
            messages.error(request, f"{field}: {error}")  # Enviar mensaje de error
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def sector_update(request, pk):
    try:
        sector = Sectores.objects.get(co_sector=pk)
        parroquia = Parroquias.objects.get(co_parroquia=request.data.get('parroquia'))
        
        serializer = SectorSerializer(sector, data={
            'co_sector': request.data.get('co_sector'),
            'des_sector': request.data.get('des_sector'),
            'parroquia': parroquia.co_parroquia
        })
        
        if serializer.is_valid():
            serializer.save(us_mo=request.user.username)
            return Response({'message': 'Sector actualizado exitosamente.'}, status=200)
        else:
            return Response(serializer.errors, status=400)
    except Sectores.DoesNotExist:
        return Response({'error': 'Sector no encontrado.'}, status=404)
    except Parroquias.DoesNotExist:
        return Response({'error': 'Parroquia no encontrada.'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['DELETE'])
def sector_delete(request, pk):
    sector = Sectores.objects.get(pk=pk)
    sector.delete()
    return Response({'message': 'Sector eliminado exitosamente.'}, status=204)

# Vistas para Entidades
class EntidadesListView(LoginRequiredMixin, ListView):
    model = Entidades
    template_name = 'pages/entidades.html'
    context_object_name = 'registros'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(nombre__icontains=search)
        return queryset.order_by('nombre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_registros'] = self.get_queryset().count()
        return context

@api_view(['POST'])
def entidades_create(request):
    serializer = EntidadesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(us_in=request.user.username)
        return Response({'message': 'Entidades creado exitosamente.'}, status=201)
    else:
        for field, error in serializer.errors.items():
            messages.error(request, f"{field}: {error}")
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def entidades_update(request, pk):
    try:
        entidades = Entidades.objects.get(pk=pk)
        serializer = EntidadesSerializer(entidades, data=request.data)
        if serializer.is_valid():
            serializer.save(us_mo=request.user.username)
            return Response({'message': 'Entidades actualizado exitosamente.'}, status=200)
        else:
            return Response(serializer.errors, status=400)
    except Entidades.DoesNotExist:
        return Response({'error': 'Entidades no encontrado.'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['DELETE'])
def entidades_delete(request, pk):
    try:
        entidades = Entidades.objects.get(pk=pk)
        entidades.delete()
        return Response({'message': 'Entidades eliminado exitosamente.'}, status=204)
    except Entidades.DoesNotExist:
        return Response({'error': 'Entidades no encontrado.'}, status=404)

# Vista para ver el detalle de un entidades
class EntidadesDetailView(LoginRequiredMixin, DetailView):
    model = Entidades
    template_name = 'pages/entidades_detail.html'
    context_object_name = 'entidades'

@api_view(['GET'])
def entidades_detail(request, pk):
    try:
        entidades = Entidades.objects.get(pk=pk)
        serializer = EntidadesSerializer(entidades)
        return Response(serializer.data)
    except Entidades.DoesNotExist:
        return Response({'error': 'Entidades no encontrado.'}, status=404)

# Vistas para Representantes
class RepresentantesListView(LoginRequiredMixin, ListView):
    model = Representantes
    template_name = 'pages/representantes.html'
    context_object_name = 'registros'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(nombre__icontains=search)
        return queryset.order_by('cedula')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entidades'] = Entidades.objects.filter(status=True)
        context['total_registros'] = self.get_queryset().count()
        return context

@api_view(['POST'])
def representantes_create(request):
    print("Datos recibidos:", request.data)  # Log para verificar los datos recibidos
    serializer = RepresentanteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(us_in=request.user.username)
        print("Representante creado exitosamente")  # Log para confirmar creación
        return Response({'message': 'Representante creado exitosamente.'}, status=201)
    else:
        print("Errores de validación:", serializer.errors)  # Log para errores de validación
        for field, error in serializer.errors.items():
            messages.error(request, f"{field}: {error}")
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def representantes_update(request, pk):
    try:
        representante = Representantes.objects.get(pk=pk)
        serializer = RepresentanteSerializer(representante, data=request.data)
        if serializer.is_valid():
            serializer.save(us_mo=request.user.username)
            return Response({'message': 'Representante actualizado exitosamente.'}, status=200)
        else:
            return Response(serializer.errors, status=400)
    except Representantes.DoesNotExist:
        return Response({'error': 'Representante no encontrado.'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['DELETE'])
def representantes_delete(request, pk):
    try:
        representante = Representantes.objects.get(pk=pk)
        representante.delete()
        return Response({'message': 'Representante eliminado exitosamente.'}, status=204)
    except Representantes.DoesNotExist:
        return Response({'error': 'Representante no encontrado.'}, status=404)

# Vista para ver el detalle de un representante
class RepresentantesDetailView(LoginRequiredMixin, DetailView):
    model = Representantes
    template_name = 'pages/representantes_detail.html'
    context_object_name = 'representante'

@api_view(['GET'])
def representantes_detail(request, pk):
    try:
        representante = Representantes.objects.get(pk=pk)
        serializer = RepresentanteSerializer(representante)
        return Response(serializer.data)
    except Representantes.DoesNotExist:
        return Response({'error': 'Representante no encontrado.'}, status=404)
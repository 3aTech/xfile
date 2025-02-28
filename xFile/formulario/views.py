from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import (Datos, Ambientes, Linderos, Representantes, Tipologias_URB,
                     Estados, Municipios, Parroquias, Sectores, Entidades, Urbanismos)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import (DatosSerializer, 
                          AmbienteSerializer, LinderoSerializer, TipologiasSerializer,
                          EstadoSerializer, MunicipioSerializer, ParroquiaSerializer, SectorSerializer,
                          EntidadesSerializer, RepresentanteSerializer, UrbanismoSerializer)
from rest_framework import status
from django.db.models import ProtectedError
from .fucnNumeroLetras import numero_a_letras, numero_a_moneda

@api_view(['GET'])
def get_numToWord(request, pk):
    if not pk:
        return Response({"error": "EL valor es requerido."}, status=status.HTTP_400_BAD_REQUEST)
    word = numero_a_letras(pk)
    return Response({"success": word})

@api_view(['GET'])
def get_numToMony(request, pk):
    if not pk:
        return Response({"error": "EL valor es requerido."}, status=status.HTTP_400_BAD_REQUEST)
    word = numero_a_moneda(pk)
    return Response({"success": word})

# Vista para obtener urbanismos según el sector
@api_view(['GET'])
def get_urbanismo(request):
    sector_id = request.GET.get('sector')
    if not sector_id:
        return Response({"error": "EL sector es requerido."}, status=status.HTTP_400_BAD_REQUEST)
    urbanismos = Urbanismos.objects.filter(sector=sector_id)
    serializer = UrbanismoSerializer(urbanismos, many=True)
    return Response(serializer.data)

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
    parroquias = Parroquias.objects.filter(municipio__co_mpo=municipio_id)
    serializer = ParroquiaSerializer(parroquias, many=True)
    return Response(serializer.data)

# Vista para obtener municipios según el estado
@api_view(['GET'])
def get_municipios(request):
    estado_id = request.GET.get('estado')
    if not estado_id:
        return Response({"error": "El estado es requerido."}, status=status.HTTP_400_BAD_REQUEST)
    municipios = Municipios.objects.filter(estado__co_edo=estado_id)
    serializer = MunicipioSerializer(municipios, many=True)
    return Response(serializer.data)

# Vista para listar los datos
class DatosListView(LoginRequiredMixin, ListView):
    model = Datos
    template_name = 'pages/list_datos.html'
    context_object_name = 'registros'
    # paginate_by = 10
    
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
        context['representantes'] = Representantes.objects.filter(status=True)
        context['estados'] = Estados.objects.filter(status=True)
        context['municipios'] = Municipios.objects.filter(status=True)
        context['parroquias'] = Parroquias.objects.filter(status=True)
        context['sectores'] = Sectores.objects.filter(status=True)
        context['urbanismos'] = Urbanismos.objects.filter(status=True)
        
        return context
    
    def form_valid(self, form):
        form.instance.us_in = self.request.user.username
        messages.success(self.request, 'Datos creado exitosamente.')
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
        context['representantes'] = Representantes.objects.filter(status=True)
        context['estados'] = Estados.objects.filter(status=True)
        context['municipios'] = Municipios.objects.filter(status=True)
        context['parroquias'] = Parroquias.objects.filter(status=True)
        context['sectores'] = Sectores.objects.filter(status=True)
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
    # paginate_by = 10
    
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
    # paginate_by = 10
    
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

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(des_edo__icontains=search)
        return queryset.order_by('des_edo')

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
    try:
        estado = Estados.objects.get(pk=pk)
        estado.delete()
        return Response({'message': 'Estado eliminado exitosamente.'}, status=status.HTTP_204_NO_CONTENT)
    except ProtectedError:
        return Response(
            {'error': 'protected_relation', 'message': 'No se puede eliminar el estado porque tiene municipios asociados.'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    except Estados.DoesNotExist:
        return Response(
            {'error': 'not_found', 'message': 'Estado no encontrado.'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {'error': 'server_error', 'message': str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

# Vistas para Municipio
class MunicipioListView(LoginRequiredMixin, ListView):
    model = Municipios
    template_name = 'pages/municipios.html'
    context_object_name = 'registros'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        estado = self.request.GET.get('estado', '')
        
        if search:
            queryset = queryset.filter(des_mpo__icontains=search)
        if estado:
            queryset = queryset.filter(estado__co_edo=estado)

        return queryset.select_related('estado').order_by('estado')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estados'] = Estados.objects.filter(status=True)
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
        municipio = Municipios.objects.get(co_mpo=pk)
        estado = Estados.objects.get(co_edo=request.data.get('estado'))
        
        serializer = MunicipioSerializer(municipio, data={
            'co_mpo': request.data.get('co_mpo'),
            'des_mpo': request.data.get('des_mpo'),
            'estado': estado.co_edo,
            'status': request.data.get('status')
        })
        
        if serializer.is_valid():
            serializer.save(us_mo=request.user.username)
            return Response({'message': 'Municipio actualizado exitosamente.'}, status=200)
        else:
            # Devolver errores de validación detallados
            errors = {}
            for field, error_list in serializer.errors.items():
                errors[field] = [str(error) for error in error_list]
            return Response({'error': 'Error de validación', 'details': errors}, status=400)
    except Municipios.DoesNotExist:
        return Response({'error': 'Municipio no encontrado.'}, status=404)
    except Estados.DoesNotExist:
        return Response({'error': 'Estado no encontrado.'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['DELETE'])
def municipio_delete(request, pk):
    try:
        municipio = Municipios.objects.get(pk=pk)
        municipio.delete()
        return Response({'message': 'Municipio eliminado exitosamente.'}, status=status.HTTP_204_NO_CONTENT)
    except ProtectedError:
        return Response(
            {'error': 'protected_relation', 'message': 'No se puede eliminar el municipios porque tiene parroquias asociadas.'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    except Estados.DoesNotExist:
        return Response(
            {'error': 'not_found', 'message': 'Municipios no encontrado.'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {'error': 'server_error', 'message': str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

# Vistas para Parroquia
class ParroquiaListView(LoginRequiredMixin, ListView):
    model = Parroquias
    template_name = 'pages/parroquias.html'
    context_object_name = 'registros'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        municipio = self.request.GET.get('municipio', '')
        estado = self.request.GET.get('estado', '')
        
        if search:
            queryset = queryset.filter(des_pquia__icontains=search)
        if municipio:
            queryset = queryset.filter(municipio__co_mpo=municipio)
        if estado:
            queryset = queryset.filter(estado__co_edo=estado)    

        return queryset.select_related('estado', 'municipio').order_by('des_pquia')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['municipios'] = Municipios.objects.filter(status=True)
        context['estados'] = Estados.objects.filter(status=True)
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
        parroquia = Parroquias.objects.get(co_pquia=pk)
        estado = Estados.objects.get(co_edo=request.data.get('estado'))
        municipio = Municipios.objects.get(co_mpo=request.data.get('municipio'))
        
        serializer = ParroquiaSerializer(parroquia, data={
            'co_pquia': request.data.get('co_pquia'),
            'des_pquia': request.data.get('des_pquia'),
            'estado': estado.co_edo,
            'municipio': municipio.co_mpo,
            'status': request.data.get('status')
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
    try:
        parroquia = Parroquias.objects.get(pk=pk)
        parroquia.delete()
        return Response({'message': 'Parroquia eliminada exitosamente.'}, status=status.HTTP_200_OK)
    except ProtectedError:
        return Response(
            {'error': 'protected_relation', 'message': 'No se puede eliminar la Parroquia porque tiene sectores asociados.'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    except Parroquias.DoesNotExist:
        return Response(
            {'error': 'not_found', 'message': 'Parroquia no encontrada.'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {'error': 'server_error', 'message': str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# Vistas para Sector
class SectorListView(LoginRequiredMixin, ListView):
    model = Sectores
    template_name = 'pages/sectores.html'
    context_object_name = 'registros'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        parroquia = self.request.GET.get('parroquia', '')
        
        if search:
            queryset = queryset.filter(des_sec__icontains=search)
        if parroquia:
            queryset = queryset.filter(parroquia__co_pquia=parroquia)

        return queryset.select_related('estado', 'municipio', 'parroquia').order_by('des_sec')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estados'] = Estados.objects.filter(status=True)
        context['municipios'] = Municipios.objects.filter(status=True)
        context['parroquias'] = Parroquias.objects.filter(status=True)
        
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
        sector = Sectores.objects.get(id=pk)  # Buscar el sector por ID
        serializer = SectorSerializer(sector, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(us_mo=request.user.username)
            return Response({'message': 'Sector actualizado exitosamente.'}, status=200)
        else:
            return Response(serializer.errors, status=400)
    except Sectores.DoesNotExist:
        return Response({'error': 'Sector no encontrado.'}, status=404)

@api_view(['DELETE'])
def sector_delete(request, pk):
    try:
        sector = Sectores.objects.get(pk=pk)
        sector.delete()
        return Response({'message': 'Sector eliminado exitosamente.'}, status=status.HTTP_200_OK)
    except ProtectedError:
        return Response(
            {'error': 'protected_relation', 'message': 'No se puede eliminar el Sector porque tiene urbanismos asociados.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
    except Estados.DoesNotExist:
        return Response(
            {'error': 'not_found', 'message': 'Sector no encontrado.'}, 
                status=status.HTTP_404_NOT_FOUND
            )
    except Exception as e:
        return Response(
            {'error': 'server_error', 'message': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

# Vistas para Entidades
class EntidadesListView(LoginRequiredMixin, ListView):
    model = Entidades
    template_name = 'pages/entidades.html'
    context_object_name = 'registros'

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
        return Response({'message': 'Entidad eliminada exitosamente.'}, status=status.HTTP_204_NO_CONTENT)
    except ProtectedError:
        return Response(
            {'error': 'protected_relation', 'message': 'No se puede eliminar la entidad porque tiene responsables asociados.'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
    except Estados.DoesNotExist:
        return Response(
            {'error': 'not_found', 'message': 'Entidad no encontrada.'}, 
                status=status.HTTP_404_NOT_FOUND
            )
    except Exception as e:
        return Response(
            {'error': 'server_error', 'message': str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

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
    serializer = RepresentanteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(us_in=request.user.username)
        return Response({'message': 'Representante creado exitosamente.'}, status=201)
    else:
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
        return Response({'message': 'Representante eliminado exitosamente.'}, status=status.HTTP_200_OK)
    except ProtectedError:
        return Response(
            {'error': 'protected_relation', 'message': 'No se puede eliminar el Representante.'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    except Parroquias.DoesNotExist:
        return Response(
            {'error': 'not_found', 'message': 'Representante no encontrado.'}, 
            status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response(
            {'error': 'server_error', 'message': str(e)}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        ) 

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


# Vista para manejar las solicitudes AJAX para crear, editar y eliminar Urbanismos
@api_view(['POST'])
def urbanismo_create(request):
    serializer = UrbanismoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(us_in=request.user.username)
        return Response({'message': 'Urbanismo creado exitosamente.'}, status=201)
    else:
        # Devolver errores de validación detallados
        errors = {}
        for field, error_list in serializer.errors.items():
            errors[field] = [str(error) for error in error_list]
        return Response({'error': 'Error de validación', 'details': errors}, status=400)

@api_view(['PUT'])
def urbanismo_update(request, pk):
    try:
        urbanismo = Urbanismos.objects.get(id=pk)
        serializer = UrbanismoSerializer(urbanismo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(us_mo=request.user.username)
            return Response({'message': 'Urbanismo actualizado exitosamente.'}, status=200)
        else:
            # Devolver errores de validación detallados
            errors = {}
            for field, error_list in serializer.errors.items():
                errors[field] = [str(error) for error in error_list]
            return Response({'error': 'Error de validación', 'details': errors}, status=400)
    except Urbanismos.DoesNotExist:
        return Response({'error': 'Urbanismo no encontrado.'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['DELETE'])
def urbanismo_delete(request, pk):
    try:
        urbanismo = Urbanismos.objects.get(id=pk)
        urbanismo.delete()
        return Response({'message': 'Urbanismo eliminado exitosamente.'}, status=200)
    except Urbanismos.DoesNotExist:
        return Response({'error': 'Urbanismo no encontrado.'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# Vista basada en clase para listar Urbanismos
class UrbanismoListView(LoginRequiredMixin, ListView):
    model = Urbanismos
    template_name = 'pages/urbanismos.html'
    context_object_name = 'registros'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(des_urb__icontains=search)
        return queryset.select_related('tipologia', 'estado', 'municipio', 'parroquia', 'sector').order_by('des_urb')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estados'] = Estados.objects.filter(status=True)
        context['municipios'] = Municipios.objects.filter(status=True)
        context['parroquias'] = Parroquias.objects.filter(status=True)
        context['sectores'] = Sectores.objects.filter(status=True)
        context['tipologias'] = Tipologias_URB.objects.filter(status=True)

        return context
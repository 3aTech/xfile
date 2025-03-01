from rest_framework import serializers
from .models import (Datos, Ambientes, Linderos, 
                     Estados, Municipios, Parroquias, Sectores, Urbanismos, Entidades, Representantes,
                     Tipologias_URB)

class DatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datos
        fields = [
                    'serial_cliente', 'expediente', 'contrato_nro', 'representante', 'sello_dorado', 'nro_dorado_oficio',  
        'cedula', 'identificador', 'denominara', 'ciudadano_ciudadana', 'nombre1', 'nombre2', 'apellido1', 'apellido2',
        'estado', 'municipio', 'parroquia', 'sector', 'urbanismo', 'torre', 'piso', 'apartamento', 'metros_cuadrados',
        'lindero_norte', 'lindero_sur', 'lindero_este', 'lindero_oeste', 'ambientes',
        'monto_credito', 'precio_venta', 'precio_venta_divisa', 'inicial', 'inicial_divisa','inicial_porcentaje',  
        'anios', 'meses', 'cuota_mensual', 'cuota_mensual_divisa', 'flat', 'flat_divisa',
        'cuota_financiera', 'cuota_financiera_divisa', 'fongar', 'fongar_divisa',
        'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo'
        ]

class AmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambientes
        fields = ['id', 'ambiente', 'status',
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']

class LinderoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Linderos
        fields = ['id', 'lindero', 'status',
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estados
        fields = ['co_edo', 'des_edo', 'iso_3166_2', 'status',
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipios
        fields = ['co_mpo', 'des_mpo', 'estado', 'status',
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']

class ParroquiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parroquias
        fields = ['co_pquia', 'des_pquia', 'estado', 'municipio', 'status',
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sectores
        fields = ['id', 'des_sec', 'estado', 'municipio', 'parroquia', 'status',
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']

class UrbanismoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urbanismos
        fields = ['id', 'des_urb', 'direccion', 'estado',
                  'municipio', 'parroquia', 'sector', 'status',
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']

class EntidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidades
        fields = ['id', 'rif', 'nombre', 'denominara', 'direccion', 'status', 'representante',
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']

class RepresentanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representantes
        fields = ['cedula', 'nacionalidad', 'ciudadano_ciudadana', 'nombre', 
                  'entidad', 'condicion', 'region', 'status',
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']

class TipologiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipologias_URB
        fields = ['id', 'tipologia', 'status',
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']


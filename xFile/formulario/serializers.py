from rest_framework import serializers
from .models import (Datos, Ambientes, Linderos, Representantes, 
                     Estados, Municipios, Parroquias, Sectores, Entidades)

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

class RepresentanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representantes
        fields = ['cedula', 'nacionalidad', 'ciudadano_ciudadana', 'nombre', 
                  'id_entidades', 'denominara', 'condicion', 'region', 'inactivo',
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estados
        fields = ['co_estado', 'des_estado', 'status',
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipios
        fields = ['co_municipio', 'des_municipio', 'estado', 'status',
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']

class ParroquiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parroquias
        fields = ['co_parroquia', 'des_parroquia', 'municipio', 'status',
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sectores
        fields = ['co_sector', 'des_sector', 'parroquia', 'status',
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']

class EntidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidades
        fields = ['id', 'rif', 'nombre', 'denominara', 'status',
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']




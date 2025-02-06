from rest_framework import serializers
from .models import (Datos, Ambiente, Lindero, Representante, 
                     Estado, Municipio, Parroquia, Sector)

class DatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datos
        fields = [
            'serial_cliente', 'sello_dorado', 'nro_dorado_oficio','cedula', 'nombre1', 'nombre2', 'apellido1', 'apellido2',
            'urbanismo', 'torre', 'piso', 'apartamento', 'monto_credito', 'precio_venta', 'precio_venta_divisa',
            'inicial', 'inicial_porcentaje', 'identificador', 'denominara', 'ciudadano_ciudadana',
            'anios', 'meses', 'cuota_mensual', 'cuota_mensual_divisa', 'flat', 'flat_divisa',
            'cuota_financiera', 'cuota_financiera_divisa', 'fongar', 'fongar_divisa', 'expediente',
            'contrato_nro', 'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo'
        ]

class AmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambiente
        fields = ['id', 'ambiente', 
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']

class LinderoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lindero
        fields = ['id', 'lindero', 
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']

class RepresentanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representante
        fields = ['cedula', 'nacionalidad', 'nombre', 'representante', 'condicion', 
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['co_estado', 'des_estado', 
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = ['co_municipio', 'des_municipio', 'estado', 
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']

class ParroquiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parroquia
        fields = ['co_parroquia', 'des_parroquia', 'municipio', 
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = ['co_sector', 'des_sector', 'parroquia', 
                  'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo']
    


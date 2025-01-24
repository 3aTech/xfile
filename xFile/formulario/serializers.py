from rest_framework import serializers
from .models import Datos

class DatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datos
        fields = [
            'serial_cliente', 'sello_dorado', 'cedula', 'nombre1', 'nombre2', 'apellido1', 'apellido2',
            'urbanismo', 'torre', 'piso', 'apartamento', 'monto_credito', 'precio_venta', 'precio_venta_divisa',
            'inicial', 'inicial_porcentaje', 'identificador', 'denominara', 'ciudadano_ciudadana',
            'anios', 'meses', 'cuota_mensual', 'cuota_mensual_divisa', 'flat', 'flat_divisa',
            'cuota_financiera', 'cuota_financiera_divisa', 'fongar', 'fongar_divisa', 'expediente',
            'contrato_nro', 'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo'
        ]
    


from rest_framework import serializers
from .models import Datos

class DatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datos
        fields = [
            'serial_cliente', 'sello_dorado', 'cedula', 'nombre1', 'nombre2', 'apellido1', 'apellido2',
            'torre', 'piso', 'apartamento', 'monto_credito', 'precio_venta', 'precio_venta_divisa',
            'inicial', 'inicial_porcentaje', 'identificador', 'denominara', 'ciudadano_ciudadana',
            'anios', 'meses', 'cuota_mensual', 'cuota_mensual_divisa', 'flat', 'flat_divisa',
            'cuota_financiera', 'cuota_financiera_divisa', 'fongar', 'fongar_divisa', 'expediente',
            'contrato_nro', 'us_in', 'fe_us_in', 'us_mo', 'fe_us_mo'
        ]

    # Validaciones personalizadas
    def validate_cedula(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("La cédula debe contener solo números.")
        return value

    def validate(self, data):
        if data['sello_dorado'] and not data['expediente']:
            raise serializers.ValidationError("El expediente es obligatorio si el sello dorado está activo.")
        return data
    


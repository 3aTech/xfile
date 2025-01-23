from django.contrib import admin
from .models import Datos
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class DatosResource(resources.ModelResource):
    class Meta:
        model = Datos

class DatosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['serial_cliente', 'nombre1', 'apellido1']
    list_display = ['serial_cliente', 'nombre1', 'apellido1', 'monto_credito', 'precio_venta', 'contrato_nro']
    resource_class = DatosResource

admin.site.register(Datos, DatosAdmin)


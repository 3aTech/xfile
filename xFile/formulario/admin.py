from django.contrib import admin
from .models import Datos, Contratos
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

class ContratosResource(resources.ModelResource):
    class Meta:
        model = Contratos

class ContratosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'serial_cliente']
    list_display = ['id', 'serial_cliente', 'url_contrato']
    resource_class = ContratosResource

admin.site.register(Contratos, ContratosAdmin)




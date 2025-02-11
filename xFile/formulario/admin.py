from django.contrib import admin
from .models import Datos, Contratos, Estados, Municipios, Parroquias, Sectores, Representantes
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
    list_display = ['id', 'serial_cliente', 'file_contrato']
    resource_class = ContratosResource

admin.site.register(Contratos, ContratosAdmin)



class EstadosResource(resources.ModelResource):
    class Meta:
        model = Estados

class EstadosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['co_estado', 'des_estado']
    list_display = ['co_estado', 'des_estado']
    resource_class = EstadosResource

admin.site.register(Estados, EstadosAdmin)



class MunicipiosResource(resources.ModelResource):
    class Meta:
        model = Municipios

class MunicipiosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['co_municipio', 'des_municipio']
    list_display = ['co_municipio', 'des_municipio']
    resource_class = MunicipiosResource

admin.site.register(Municipios, MunicipiosAdmin)



class ParroquiasResource(resources.ModelResource):
    class Meta:
        model = Parroquias

class ParroquiasAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['co_parroquia', 'des_parroquia']
    list_display = ['co_parroquia', 'des_parroquia']
    resource_class = ParroquiasResource

admin.site.register(Parroquias, ParroquiasAdmin)



class SectoresResource(resources.ModelResource):
    class Meta:
        model = Sectores

class SectoresAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['co_sector', 'des_sector']
    list_display = ['co_sector', 'des_sector']
    resource_class = SectoresResource

admin.site.register(Sectores, SectoresAdmin)



class RepresentantesResource(resources.ModelResource):
    class Meta:
        model = Representantes

class RepresentantesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['cedula', 'nombre']
    list_display = ['cedula', 'nombre']
    resource_class = RepresentantesResource

admin.site.register(Representantes, RepresentantesAdmin)



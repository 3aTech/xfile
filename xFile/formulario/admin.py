from django.contrib import admin
from .models import Datos, Contratos, Estados, Municipios, Parroquias, Sectores, Urbanismos, Representantes, Entidades
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
    search_fields = ['co_edo', 'des_edo']
    list_display = ['co_edo', 'des_edo', 'iso_3166_2']
    resource_class = EstadosResource

admin.site.register(Estados, EstadosAdmin)



class MunicipiosResource(resources.ModelResource):
    class Meta:
        model = Municipios

class MunicipiosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['co_mpo', 'des_mpo', 'estado']
    list_display = ['co_mpo', 'des_mpo', 'estado']
    resource_class = MunicipiosResource

admin.site.register(Municipios, MunicipiosAdmin)



class ParroquiasResource(resources.ModelResource):
    class Meta:
        model = Parroquias

class ParroquiasAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['co_pquia', 'des_pquia']
    list_display = ['co_pquia', 'des_pquia']
    resource_class = ParroquiasResource

admin.site.register(Parroquias, ParroquiasAdmin)



class SectoresResource(resources.ModelResource):
    class Meta:
        model = Sectores

class SectoresAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['co_sec', 'des_sec']
    list_display = ['co_sec', 'des_sec']
    resource_class = SectoresResource

admin.site.register(Sectores, SectoresAdmin)



class UrbanismosResource(resources.ModelResource):
    class Meta:
        model = Urbanismos

class UrbanismosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'des_urb']
    list_display = ['id', 'des_urb']
    resource_class = UrbanismosResource

admin.site.register(Urbanismos, UrbanismosAdmin)



class RepresentantesResource(resources.ModelResource):
    class Meta:
        model = Representantes

class RepresentantesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['cedula', 'nombre']
    list_display = ['cedula', 'nombre']
    resource_class = RepresentantesResource

admin.site.register(Representantes, RepresentantesAdmin)



class EntidadesResource(resources.ModelResource):
    class Meta:
        model = Entidades

class EntidadesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id', 'rif', 'nombre']
    list_display = ['id', 'rif', 'nombre']
    resource_class = EntidadesResource

admin.site.register(Entidades, EntidadesAdmin)



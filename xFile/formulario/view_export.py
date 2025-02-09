from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import (
                    Datos,)

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status

from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.worksheet.table import Table, TableStyleInfo
from datetime import datetime

def exportar_datos_xlsx(request):
    # Crear un libro de trabajo y una hoja
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = 'Registros'

    # Agregar un título
    title = "Reporte de Registros"
    sheet.append([])
    sheet.append([title])  # Agregar el título en la primera fila
    sheet.merge_cells('A2:AV2')  # Fusionar celdas para el título
    sheet['A2'].font = Font(bold=True, size=14)  # Aplicar negrita y tamaño de fuente al título
    sheet.append([])
    # Escribir los encabezados
    headers = ['Serial Cliente', 'Nro. de Expediente', 'Nro de Contrato', 'Representante', 'Sello Doraro', 'Nro. de Oficio Dorado',  
               'Cédula', 'Identificador', 'Denominara', 'Ciudadano/Ciudadana', 'Primer Nombre', 'Segundo Nombre', 'Primer Apellido', 'Segundo Apellido',
               'Estado', 'Municipio', 'Parroquia', 'Sector', 'Urbanismo', 'Torre', 'Piso', 'Apartamento', 'Mtros. Cuadrados',
               'Lindero Norter', 'Lindero Sur', 'Lindero Este', 'Lindero Oeste', 'Admbientes',
               'Monto del Crédito Hipotecario a Otorgar', 'Precio Venta Bs.', 'Precio Venta $/€', 'Inicial Bs.', 'inicial $/€',' % Inicial',  
               'Años', 'Meses', 'Cuota Mensual Bs.', 'Cuota Mensual $/€', 'Flat Bs.', 'Flat $/€',
               'Cuota Financiera Requerida Bs.', 'Cuota Financiera Requerida $/€', 'Fongar Bs.', 'Fongar $/€',
               'Creado Por', 'Fecha de Creación', 'Modificado Por', 'Fecha de Modificación']  # Actualizado con los campos del modelo Datos
    sheet.append(headers)

    # Aplicar negrita a los encabezados
    for cell in sheet[4]: 
        cell.font = Font(bold=True)

    # Obtener los registros
    registros = Datos.objects.all() 

    # Escribir los datos
    for registro in registros:
        selloDorado = 'No'
        if registro.sello_dorado:
            selloDorado = 'Sí'  
            
        representante_nombre = str(registro.representante) if registro.representante else 'Sin representante'
        estado_nombre = str(registro.estado) if registro.estado else 'Sin estado'  
        municipio_nombre = str(registro.municipio) if registro.municipio else 'Sin municipio'  
        parroquia_nombre = str(registro.parroquia) if registro.parroquia else 'Sin parroquia'  
        sector_nombre = str(registro.sector) if registro.sector else 'Sin sector'  
        fecha_creacion = registro.fe_us_in.replace(tzinfo=None) if registro.fe_us_in else None
        fecha_modificacion = registro.fe_us_mo.replace(tzinfo=None) if registro.fe_us_mo else None

        sheet.append([registro.serial_cliente, registro.expediente, registro.contrato_nro, 
                      representante_nombre, selloDorado, registro.nro_dorado_oficio, 
                      registro.cedula, registro.identificador, registro.denominara, registro.ciudadano_ciudadana,
                      registro.nombre1, registro.nombre2, registro.apellido1, registro.apellido2, 
                      estado_nombre, municipio_nombre, parroquia_nombre, sector_nombre, registro.urbanismo,
                      registro.torre, registro.piso, registro.apartamento, registro.metros_cuadrados,
                      registro.lindero_norte, registro.lindero_sur, registro.lindero_este, registro.lindero_oeste, registro.ambientes,
                      registro.monto_credito, registro.precio_venta, registro.precio_venta_divisa, registro.inicial, registro.inicial_divisa, registro.inicial_porcentaje,
                      registro.anios, registro.meses, registro.cuota_mensual, registro.cuota_mensual_divisa, registro.flat, registro.flat_divisa,
                      registro.cuota_financiera, registro.cuota_financiera_divisa, registro.fongar, registro.fongar_divisa,
                      registro.us_in, fecha_creacion, registro.us_mo, fecha_modificacion
                      ])  # Actualizado con los campos del modelo Datos

    # Crear una tabla
    tab = Table(displayName="TablaRegistros", ref=f"A4:AV{len(registros) + 4}")  # Ajustar el rango para incluir el título

    # Estilo de la tabla
    style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False, showRowStripes=True, showColumnStripes=True)
    tab.tableStyleInfo = style

    # Añadir la tabla a la hoja
    sheet.add_table(tab)

    fecha = datetime.now().strftime('%Y-%m-%d')
    # Crear la respuesta HTTP
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="registros_{fecha}.xlsx"'
    
    # Guardar el libro de trabajo en la respuesta
    workbook.save(response)
    return response



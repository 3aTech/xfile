from django.templatetags.static import static
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import (
                    Datos,
                    Contratos,)

from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import status

from datetime import datetime
from docx import Document


def genContratosTotales(request):
    registros = Datos.objects.all() 

    generar_docx_desde_plantilla(registros)

    # Redirigir a otra vista
    return redirect('datos_list')  # Reemplaza 'nombre_de_la_vista' con el nombre de la vista a la que deseas redirigir

def genContratosUnico(request, pk):
    registro = Datos.objects.get(pk=pk) 
    
    generar_docx_desde_plantilla(registro)   



def generar_docx_desde_plantilla(registros):
    """
    Genera un archivo .docx basado en una plantilla, reemplazando los placeholders.

    Args:
        reemplazos (dict): Diccionario con los placeholders y sus valores.
    """
    ruta_plantilla = static('3atech/media/plantillas/modelo_venta_a_plazo.docx')
    ruta_salida = static('3atech/media/Contratos')

    contrato = 0
    for registro in registros:
        contrato +=1 
        # Crear una copia de la plantilla
        doc = Document(ruta_plantilla)
    
        # Reemplazar placeholders en cada párrafo
        for parrafo in doc.paragraphs:
            for placeholder, valor in registro.__dict__.items():
                if placeholder in parrafo.text:
                    parrafo.text = parrafo.text.replace(placeholder, str(valor))
    
    # Reemplazar placeholders en tablas (opcional)
    for tabla in doc.tables:
        for fila in tabla.rows:
            for celda in fila.cells:
                for placeholder, valor in registro.__dict__.items():
                    if placeholder in celda.text:
                        celda.text = celda.text.replace(placeholder, str(valor))
    
    # Guardar el archivo generado
    nombre_archivo = f"{ruta_salida}/contrato_{contrato}.docx"
    doc.save(nombre_archivo)
    
    # Guardar la ruta en el modelo Contratos
    contrato_obj = Contratos.objects.create(
            serial_cliente=registro,  # Asignar el objeto Datos
            url_contrato=nombre_archivo  # Guardar la ruta del archivo
        )

registros = [
    {
        "{nombre}": "Alexis",
        "{fecha}": "21 de enero de 2025",
        "{mensaje}": "¡Este es un ejemplo generado dinámicamente!"
    }
]

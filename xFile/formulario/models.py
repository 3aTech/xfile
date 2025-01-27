from django.db import models

class ModeloAuditoria(models.Model):
    """Modelo base abstracto para campos de auditoría"""
    us_in = models.CharField('Creado por', max_length=150, null=True, blank=True)
    fe_us_in = models.DateTimeField('Fecha de Creación', auto_now_add=True)
    us_mo = models.CharField('Modificado por', max_length=150, null=True, blank=True)
    fe_us_mo = models.DateTimeField('Fecha de Modificación', auto_now=True)

    class Meta:
        abstract = True

class Datos(ModeloAuditoria):
    """Modelo que representa las monedas."""
    serial_cliente = models.CharField('Serial', help_text='Serial Cliente', max_length=10, primary_key=True, unique=True)
    sello_dorado = models.BooleanField('Sello Dorado', default=False, help_text='Sello Dorado')
    cedula = models.CharField('Cédula', max_length=12, help_text='Cédula')
    nombre1 = models.CharField('Nombre 1', max_length=20, help_text='Nombre 1')
    nombre2 = models.CharField('Nombre 2', max_length=20, help_text='Nombre 2', null=True, blank=True)
    apellido1 = models.CharField('Apellido 1', max_length=20, help_text='Apellido 1')
    apellido2 = models.CharField('Apellido 2', max_length=20, help_text='Apellido 2', null=True, blank=True)
    urbanismo = models.CharField('Urbanismo', max_length=120, help_text='Urbanismo')
    torre = models.CharField('Torre', max_length=10, help_text='Torre')
    piso = models.CharField('Piso', max_length=8, help_text='Piso')
    apartamento = models.CharField('Apartamento', max_length=8, help_text='Apartamento')
    monto_credito = models.DecimalField('Monto Crédito', max_digits=18, decimal_places=8, help_text='Monto Crédito Hipotecario a Otorgar')
    precio_venta = models.DecimalField('Precio Venta', max_digits=18, decimal_places=8, help_text='Precio de Venta')
    precio_venta_divisa = models.DecimalField('Precio Venta Divisa', max_digits=18, decimal_places=8, help_text='Precio de Venta en Divisa')
    inicial = models.DecimalField('Inicial', max_digits=18, decimal_places=8, help_text='Inicial')
    inicial_porcentaje = models.DecimalField('% Inicial', max_digits=18, decimal_places=8, help_text='% Inicial')
    identificador = models.CharField('Identificado', max_length=3, help_text='Identificado')
    denominara = models.CharField('Denominara', max_length=20, help_text='Denominara')
    ciudadano_ciudadana = models.CharField('Ciudadano/Ciudadana', max_length=20, help_text='Ciudadano/Ciudadana')
    anios = models.CharField('Años', max_length=4, help_text='Años')
    meses = models.CharField('Meses', max_length=3, help_text='Meses')
    cuota_mensual = models.DecimalField('Cuota Mensual', max_digits=18, decimal_places=8, help_text='Cuota Mensual')
    cuota_mensual_divisa = models.DecimalField('Cuota Mensual Divisa', max_digits=18, decimal_places=8, help_text='Cuota Mensual Divisa')
    flat = models.DecimalField('Flat Hipotecario', max_digits=18, decimal_places=8, help_text='Flat Hipotecario')
    flat_divisa = models.DecimalField('Flat Hipotecario Divisa', max_digits=18, decimal_places=8, help_text='Flat Hipotecario Divisa')
    cuota_financiera = models.DecimalField('Cuota Financiera', max_digits=18, decimal_places=8, help_text='Cuota Financiera')
    cuota_financiera_divisa = models.DecimalField('Cuota Financiera Divisa', max_digits=18, decimal_places=8, help_text='Cuota Financiera Divisa')
    fongar = models.DecimalField('Fongar', max_digits=18, decimal_places=8, help_text='Fongar')
    fongar_divisa = models.DecimalField('Fongar Divisa', max_digits=18, decimal_places=8, help_text='Fongar Divisa')
    expediente = models.CharField('Expediente', max_length=50, help_text='Expediente', null=True, blank=True)
    contrato_nro = models.CharField('Nro. Contrato', max_length=50, help_text='Nro. Contrato', null=True, blank=True) 
    
    def __str__(self) -> str:
        return f'{self.expediente} ({self.nombre1}) ({self.apellido1})'
    
    def get_full_name(self):
        return f'{self.contrato_nro} - {self.expediente} - {self.nombre1} {self.apellido1}'

    def get_short_name(self):
        return self.nombre1
    
    def save(self, *args, **kwargs):
        self.us_in = self.us_in or kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['serial_cliente']
        verbose_name = 'Dato'
        verbose_name_plural = 'Datos'
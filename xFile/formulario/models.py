from django.db import models

class ModeloAuditoria(models.Model):
    """Modelo base abstracto para campos de auditoría"""
    us_in = models.CharField('Creado por', max_length=150, null=True, blank=True)
    fe_us_in = models.DateTimeField('Fecha de Creación', auto_now_add=True)
    us_mo = models.CharField('Modificado por', max_length=150, null=True, blank=True)
    fe_us_mo = models.DateTimeField('Fecha de Modificación', auto_now=True)

    class Meta:
        abstract = True

class Ambiente(ModeloAuditoria):
    """Modelo para almacenar ambientes"""
    id = models.AutoField('Código', help_text='Código', primary_key=True)
    ambiente = models.CharField('Ambiente', help_text='Ambiente', max_length=60)

    def __str__(self) -> str:
        return f'{self.co_estado} - {self.des_estado}'

    class Meta:
        verbose_name = 'Ambiente'
        verbose_name_plural = 'Ambientes'
        ordering = ['ambiente']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        super().save(*args, **kwargs)

class Lindero(ModeloAuditoria):
    """Modelo para almacenar linderos"""
    id = models.AutoField('Código', help_text='Código', primary_key=True)
    lindero = models.CharField('Lindero', max_length=255, help_text='Lindero')

    def __str__(self) -> str:
        return f'{self.id} - {self.descripcion}'

    class Meta:
        verbose_name = 'Lindero'
        verbose_name_plural = 'Linderos'
        ordering = ['lindero']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        super().save(*args, **kwargs)

class Representante(ModeloAuditoria):
    """Modelo para almacenar representantes"""
    cedula = models.CharField('Cédula', help_text='Cédula del representante', max_length=12, primary_key=True)
    nacionalidad = models.CharField('Nacionalidad', help_text='Nacionalidad', max_length=120)
    nombre = models.CharField('Nombre y Apellido', help_text='Nombre y apellido del representante', max_length=120)
    representante = models.CharField('Representante de', help_text='Representante de', max_length=120)
    condicion = models.CharField('Condición y/o Caracter Representativo', help_text='Condición y/o Caracter Representativo', max_length=120)
    inactivo = models.BooleanField('Estado', default=True, help_text='Estado de actividad')
    
    def __str__(self) -> str:
        return f'{self.cedula} - {self.nombre}'

    class Meta:
        verbose_name = 'Representante'
        verbose_name_plural = 'Representantes'
        ordering = ['cedula', 'nombre']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        super().save(*args, **kwargs)

class Estado(ModeloAuditoria):
    """Modelo para almacenar estados/provincias"""
    co_estado = models.CharField('Código', help_text='Código del estado', max_length=6, primary_key=True)
    des_estado = models.CharField('Nombre', help_text='Nombre del estado', max_length=60)

    def __str__(self) -> str:
        return f'{self.co_estado} - {self.des_estado}'

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ['des_estado']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        super().save(*args, **kwargs)

class Municipio(ModeloAuditoria):
    """Modelo para almacenar municipios"""
    co_municipio = models.CharField('Código', help_text='Código del municipio', max_length=6, primary_key=True)
    des_municipio = models.CharField('Nombre', help_text='Nombre del municipio', max_length=60)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, related_name='municipios')

    def __str__(self) -> str:
        return f'{self.co_municipio} - {self.des_municipio}'

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        ordering = ['des_municipio']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        super().save(*args, **kwargs)

class Parroquia(ModeloAuditoria):
    """Modelo para almacenar parroquias"""
    co_parroquia = models.CharField('Código', help_text='Código de la parroquia', max_length=6, primary_key=True)
    des_parroquia = models.CharField('Nombre', help_text='Nombre de la parroquia', max_length=60)
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT, related_name='parroquias')

    def __str__(self) -> str:
        return f'{self.co_parroquia} - {self.des_parroquia}'

    class Meta:
        verbose_name = 'Parroquia'
        verbose_name_plural = 'Parroquias'
        ordering = ['des_parroquia']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        super().save(*args, **kwargs)

class Sector(ModeloAuditoria):
    """Modelo para almacenar sectores"""
    co_sector = models.CharField('Código', help_text='Código del sector', max_length=6, primary_key=True)
    des_sector = models.CharField('Nombre', help_text='Nombre del sector', max_length=60)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.PROTECT, related_name='sectores')

    def __str__(self) -> str:
        return f'{self.co_sector} - {self.des_sector}'

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'
        ordering = ['des_sector']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        super().save(*args, **kwargs)

class Datos(ModeloAuditoria):
    """Modelo que representa las monedas."""
    serial_cliente = models.CharField('Serial', help_text='Serial Cliente', max_length=20, primary_key=True, unique=True)
    expediente = models.CharField('Expediente', max_length=50, help_text='Expediente', null=True, blank=True)
    contrato_nro = models.CharField('Nro. Contrato', max_length=50, help_text='Nro. Contrato', null=True, blank=True) 
    representante = models.ForeignKey(Representante, on_delete=models.PROTECT, related_name='datos')
    sello_dorado = models.BooleanField('Sello Dorado', default=False, help_text='Sello Dorado')
    nro_dorado_oficio = models.CharField('Número Sello Dorado u Oficio', max_length=20, help_text='Número Sello Dorado u Oficio', null=True, blank=True)
    
    cedula = models.CharField('Cédula', max_length=12, help_text='Cédula')
    identificador = models.CharField('Identificado', max_length=3, help_text='Identificado')
    denominara = models.CharField('Denominara', max_length=20, help_text='Denominara')
    ciudadano_ciudadana = models.CharField('Ciudadano/Ciudadana', max_length=20, help_text='Ciudadano/Ciudadana')
    nombre1 = models.CharField('Nombre 1', max_length=20, help_text='Nombre 1')
    nombre2 = models.CharField('Nombre 2', max_length=20, help_text='Nombre 2', null=True, blank=True)
    apellido1 = models.CharField('Apellido 1', max_length=20, help_text='Apellido 1')
    apellido2 = models.CharField('Apellido 2', max_length=20, help_text='Apellido 2', null=True, blank=True)
    
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT, related_name='datos')
    municipio = models.ForeignKey(Municipio, on_delete=models.PROTECT, related_name='datos')
    parroquia = models.ForeignKey(Parroquia, on_delete=models.PROTECT, related_name='datos')
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT, related_name='datos')
    urbanismo = models.CharField('Urbanismo', max_length=120, help_text='Urbanismo')
    torre = models.CharField('Torre', max_length=10, help_text='Torre')
    piso = models.CharField('Piso', max_length=8, help_text='Piso')
    apartamento = models.CharField('Apartamento', max_length=8, help_text='Apartamento')
    metros_cuadrados = models.DecimalField('Mtrs2', max_digits=18, decimal_places=2, help_text='Mtrs2')
    
    lindero_norte = models.CharField('Lindero Norte', max_length=20, help_text='Lindero Norte', null=True, blank=True)
    lindero_sur = models.CharField('Lindero Sur', max_length=20, help_text='Lindero Sur', null=True, blank=True)
    lindero_este = models.CharField('Lindero Este', max_length=20, help_text='Lindero Este', null=True, blank=True)
    lindero_oeste = models.CharField('Lindero Oeste', max_length=20, help_text='Lindero Oeste', null=True, blank=True)
    ambientes = models.CharField('Datos de Ambientes', max_length=300, help_text='Datos de Ambientes', null=True, blank=True)
    
    monto_credito = models.DecimalField('Monto Crédito', max_digits=18, decimal_places=8, help_text='Monto Crédito Hipotecario a Otorgar')
    precio_venta = models.DecimalField('Precio Venta', max_digits=18, decimal_places=8, help_text='Precio de Venta')
    precio_venta_divisa = models.DecimalField('Precio Venta Divisa', max_digits=18, decimal_places=8, help_text='Precio de Venta en Divisa')
    inicial = models.DecimalField('Inicial', max_digits=18, decimal_places=8, help_text='Inicial')
    inicial_porcentaje = models.DecimalField('% Inicial', max_digits=18, decimal_places=8, help_text='% Inicial')
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
        
class Ambiente_Dato(ModeloAuditoria):
    """Modelo para almacenar ambientes de los datos"""
    id = models.AutoField('Código', help_text='Código', primary_key=True)
    id_ambiente = models.ForeignKey(Ambiente, on_delete=models.PROTECT, related_name='Ambiente_Dato')
    serial_cliente = models.ForeignKey(Datos, on_delete=models.PROTECT, related_name='ambiente_datos')

    def __str__(self) -> str:
        return f'{self.id} - {self.serial_cliente}'

    class Meta:
        verbose_name = 'Ambiente Dato'
        verbose_name_plural = 'Ambientes Datos'
        ordering = ['serial_cliente']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        super().save(*args, **kwargs)


class Lindero_Dato(ModeloAuditoria):
    """Modelo para almacenar lineros de los datos"""
    id = models.AutoField('Código', help_text='Código', primary_key=True)
    id_lindero = models.ForeignKey(Lindero, on_delete=models.PROTECT, related_name='Lindero_Dato')
    serial_cliente = models.ForeignKey(Datos, on_delete=models.PROTECT, related_name='lindero_datos')

    def __str__(self) -> str:
        return f'{self.id} - {self.serial_cliente}'

    class Meta:
        verbose_name = 'Lindero Dato'
        verbose_name_plural = 'Linderos Datos'
        ordering = ['serial_cliente']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        super().save(*args, **kwargs)
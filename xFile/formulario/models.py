from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ModeloAuditoria(models.Model):
    """Modelo base abstracto para campos de auditoría"""
    us_in = models.ForeignKey(User, on_delete=models.PROTECT, related_name='auditoria_modelo')
    fe_us_in = models.DateTimeField('Fecha de Creación', auto_now_add=True)
    us_mo = models.CharField('Modificado por', max_length=150, null=True, blank=True)
    fe_us_mo = models.DateTimeField('Fecha de Modificación', auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        print(f'Usuario que crea: {self.us_in}, Usuario que modifica: {self.us_mo}')
        super().save(*args, **kwargs)

class Ambientes(ModeloAuditoria):
    """Modelo para almacenar ambientes"""
    id = models.AutoField('Código', help_text='Código', primary_key=True)
    ambiente = models.CharField('Ambiente', help_text='Ambiente', max_length=60)
    status = models.BooleanField('Estado', default=True, help_text='Estado de actividad')

    def __str__(self) -> str:
        return f'{self.des_estado}'

    class Meta:
        verbose_name = 'Ambiente'
        verbose_name_plural = 'Ambientes'
        ordering = ['ambiente']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        print(f'Usuario que modifica: {self.us_mo}')
        super().save(*args, **kwargs)

class Linderos(ModeloAuditoria):
    """Modelo para almacenar linderos"""
    id = models.AutoField('Código', help_text='Código', primary_key=True)
    lindero = models.CharField('Lindero', max_length=255, help_text='Lindero')
    status = models.BooleanField('Estado', default=True, help_text='Estado de actividad')

    def __str__(self) -> str:
        return f'{self.descripcion}'

    class Meta:
        verbose_name = 'Lindero'
        verbose_name_plural = 'Linderos'
        ordering = ['lindero']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        print(f'Usuario que modifica: {self.us_mo}')
        super().save(*args, **kwargs)

class Entidades(ModeloAuditoria):
    """Modelo para almacenar entidades"""
    id = models.AutoField('Código', help_text='Código', primary_key=True)
    rif = models.CharField('R.I.F.', help_text='R.I.F.', max_length=12, unique=True)
    nombre = models.CharField('Se Denominará', help_text='Se Denominará', max_length=120)
    denominara = models.CharField('Se Denominará', help_text='Se Denominará', max_length=120, null=True, blank=True)
    direccion = models.CharField('Dirección', help_text='Dirección', max_length=250, null=True, blank=True)
    status = models.BooleanField('Estado', default=True, help_text='Estado de actividad')
    
    def __str__(self) -> str:
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'Entidades'
        verbose_name_plural = 'Entidades'
        ordering = ['rif', 'nombre']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        print(f'Usuario que modifica: {self.us_mo}')
        super().save(*args, **kwargs)

class Representantes(ModeloAuditoria):
    """Modelo para almacenar representantes"""
    cedula = models.CharField('Cédula', help_text='Cédula del representante', max_length=12, primary_key=True)
    nacionalidad = models.CharField('Nacionalidad', help_text='Nacionalidad', max_length=120)
    ciudadano_ciudadana = models.CharField('Ciudadano/Ciudadana', max_length=20, help_text='Ciudadano/Ciudadana')
    nombre = models.CharField('Nombre y Apellido', help_text='Nombre y apellido del representante', max_length=120)
    entidad = models.ForeignKey(Entidades, on_delete=models.PROTECT, related_name='representante')
    condicion = models.CharField('Condición y/o Caracter Representativo', help_text='Condición y/o Caracter Representativo', max_length=120)
    region = models.CharField('Región', help_text='Región', max_length=120)
    status = models.BooleanField('Estado', default=True, help_text='Estado de actividad')
    
    def __str__(self) -> str:
        return f'{self.nombre}'

    class Meta:
        verbose_name = 'Representante'
        verbose_name_plural = 'Representantes'
        ordering = ['cedula', 'nombre']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        print(f'Usuario que modifica: {self.us_mo}')
        super().save(*args, **kwargs)
        
class Estados(ModeloAuditoria):
    """Modelo para almacenar estados/provincias"""
    co_edo = models.CharField('Código', help_text='Código del estado', max_length=6, primary_key=True)
    des_edo = models.CharField('Nombre', help_text='Nombre del estado', max_length=60)
    iso_3166_2 = models.CharField('iso_3166-2', help_text='ISO_3166-2', max_length=4, null=True, blank=True)
    status = models.BooleanField('Estado', default=True, help_text='Estado de actividad')

    def __str__(self) -> str:
        return f'{self.des_edo}'

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ['des_edo']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        print(f'Usuario que modifica: {self.us_mo}')
        super().save(*args, **kwargs)

class Municipios(ModeloAuditoria):
    """Modelo para almacenar municipios"""
    co_mpo = models.CharField('Código', help_text='Código del municipio', max_length=6, primary_key=True)
    des_mpo = models.CharField('Nombre', help_text='Nombre del municipio', max_length=60)
    estado = models.ForeignKey(Estados, on_delete=models.PROTECT, related_name='municipios')
    status = models.BooleanField('Estado', default=True, help_text='Estado de actividad')

    def __str__(self) -> str:
        return f'{self.des_mpo}'

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'
        ordering = ['estado']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        print(f'Usuario que modifica: {self.us_mo}')
        super().save(*args, **kwargs)

class Parroquias(ModeloAuditoria):
    """Modelo para almacenar parroquias"""
    co_pquia = models.CharField('Código', help_text='Código de la parroquia', max_length=6, primary_key=True)
    des_pquia = models.CharField('Nombre', help_text='Nombre de la parroquia', max_length=60)
    estado = models.ForeignKey(Estados, on_delete=models.PROTECT, related_name='parroquias')
    municipio = models.ForeignKey(Municipios, on_delete=models.PROTECT, related_name='parroquias')
    status = models.BooleanField('Estado', default=True, help_text='Estado de actividad')

    def __str__(self) -> str:
        return f'{self.des_pquia}'

    class Meta:
        verbose_name = 'Parroquia'
        verbose_name_plural = 'Parroquias'
        ordering = ['des_pquia']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        print(f'Usuario que modifica: {self.us_mo}')
        super().save(*args, **kwargs)

class Sectores(ModeloAuditoria):
    """Modelo para almacenar sectores"""
    id = models.AutoField('Código', help_text='Código', primary_key=True)
    des_sec = models.CharField('Nombre', help_text='Nombre del sector', max_length=60)
    estado = models.ForeignKey(Estados, on_delete=models.PROTECT, related_name='sectores')
    municipio = models.ForeignKey(Municipios, on_delete=models.PROTECT, related_name='sectores')
    parroquia = models.ForeignKey(Parroquias, on_delete=models.PROTECT, related_name='sectores')
    status = models.BooleanField('Estado', default=True, help_text='Estado de actividad')

    def __str__(self) -> str:
        return f'{self.des_sec}'

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'
        ordering = ['des_sec']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        print(f'Usuario que modifica: {self.us_mo}')
        super().save(*args, **kwargs)

class Tipologias_URB(ModeloAuditoria):
    """Modelo para almacenar sectores"""
    id = models.AutoField('ID', help_text='ID', primary_key=True)
    tipologia = models.CharField('Nombre de la Tipología', max_length=255, help_text='Nombre de la Tipología')
    status = models.BooleanField('Estado', default=True, help_text='Estado de actividad')

    def __str__(self) -> str:
        return f'{self.tipologia}'

    class Meta:
        verbose_name = 'Tipología'
        verbose_name_plural = 'Tipologías'
        ordering = ['tipologia']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        print(f'Usuario que modifica: {self.us_mo}')
        super().save(*args, **kwargs)


class Urbanismos(ModeloAuditoria):
    """Modelo para almacenar sectores"""
    id = models.AutoField('Código', help_text='Código', primary_key=True)
    des_urb = models.CharField('Nombre del Urbanismo', max_length=255, help_text='Nombre del Urbanismo')
    direccion = models.CharField('Dirección', max_length=255, help_text='Dirección del Urbanismo', null=True, blank=True)
    tipologia = models.ForeignKey(Tipologias_URB, on_delete=models.PROTECT, related_name='urbanismos')
    estado = models.ForeignKey(Estados, on_delete=models.PROTECT, related_name='urbanismos', null=True, blank=True)
    municipio = models.ForeignKey(Municipios, on_delete=models.PROTECT, related_name='urbanismos', null=True, blank=True)
    parroquia = models.ForeignKey(Parroquias, on_delete=models.PROTECT, related_name='urbanismos', null=True, blank=True)
    sector = models.ForeignKey(Sectores, on_delete=models.PROTECT, related_name='urbanismos', null=True, blank=True)
    status = models.BooleanField('Estado', default=True, help_text='Estado de actividad')

    def __str__(self) -> str:
        return f'{self.des_urb}'

    class Meta:
        verbose_name = 'Urbanismo'
        verbose_name_plural = 'Urbanismos'
        ordering = ['des_urb']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        print(f'Usuario que modifica: {self.us_mo}')
        super().save(*args, **kwargs)

class Datos(ModeloAuditoria):
    """Modelo que representa las monedas."""
    serial_cliente = models.CharField('Serial', help_text='Serial Cliente', max_length=20, primary_key=True, unique=True)
    expediente = models.CharField('Expediente', max_length=50, help_text='Expediente', null=True, blank=True)
    contrato_nro = models.CharField('Nro. Contrato', max_length=50, help_text='Nro. Contrato', null=True, blank=True) 
    representante = models.ForeignKey(Representantes, on_delete=models.PROTECT, related_name='datos')
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
    
    estado = models.ForeignKey(Estados, on_delete=models.PROTECT, related_name='datos')
    municipio = models.ForeignKey(Municipios, on_delete=models.PROTECT, related_name='datos')
    parroquia = models.ForeignKey(Parroquias, on_delete=models.PROTECT, related_name='datos')
    sector = models.ForeignKey(Sectores, on_delete=models.PROTECT, related_name='datos')
    urbanismo = models.ForeignKey(Urbanismos, on_delete=models.PROTECT, related_name='datos')
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
    inicial_divisa = models.DecimalField('Inicial Divisa', max_digits=18, decimal_places=8, help_text='Inicial Divisa')
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
        print(f'Usuario que modifica: {self.us_mo}')
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['serial_cliente']
        verbose_name = 'Dato'
        verbose_name_plural = 'Datos'
        
class Ambiente_Dato(ModeloAuditoria):
    """Modelo para almacenar ambientes de los datos"""
    id = models.AutoField('Código', help_text='Código', primary_key=True)
    id_ambiente = models.ForeignKey(Ambientes, on_delete=models.PROTECT, related_name='Ambiente_Dato')
    serial_cliente = models.ForeignKey(Datos, on_delete=models.PROTECT, related_name='ambiente_datos')

    def __str__(self) -> str:
        return f'{self.serial_cliente}'

    class Meta:
        verbose_name = 'Ambiente Dato'
        verbose_name_plural = 'Ambientes Datos'
        ordering = ['serial_cliente']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        print(f'Usuario que modifica: {self.us_mo}')
        super().save(*args, **kwargs)

class Contratos(ModeloAuditoria):
    """Modelo para almacenar contratos"""
    id = models.AutoField('ID', help_text='ID', primary_key=True)
    serial_cliente = models.ForeignKey(Datos, on_delete=models.PROTECT, related_name='contatos')
    file_contrato = models.CharField(
        'Archivo', 
        max_length=30,
        help_text='Ingrese el nombre del contrato.', 
        blank=True,  # Permitir que el campo esté vacío
        null=True    # Permitir que el campo sea nulo en la base de datos
    )

    def __str__(self) -> str:
        return f'{self.serial_cliente}'
    
    def get_full_name(self):
        return f'{self.id} - {self.serial_cliente}'

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        ordering = ['serial_cliente']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        print(f'Usuario que modifica: {self.us_mo}')
        super().save(*args, **kwargs)


class Lindero_Dato(ModeloAuditoria):
    """Modelo para almacenar lineros de los datos"""
    id = models.AutoField('Código', help_text='Código', primary_key=True)
    id_lindero = models.ForeignKey(Linderos, on_delete=models.PROTECT, related_name='Lindero_Dato')
    serial_cliente = models.ForeignKey(Datos, on_delete=models.PROTECT, related_name='lindero_datos')

    def __str__(self) -> str:
        return f'{self.serial_cliente}'

    class Meta:
        verbose_name = 'Lindero Dato'
        verbose_name_plural = 'Linderos Datos'
        ordering = ['serial_cliente']

    def save(self, *args, **kwargs):
        if not self.us_in:
            self.us_in = kwargs.pop('usuario', None)
        self.us_mo = kwargs.pop('usuario_modificador', None)
        print(f'Usuario que modifica: {self.us_mo}')
        super().save(*args, **kwargs)
# Generated by Django 5.1.5 on 2025-01-24 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('us_in', models.CharField(blank=True, max_length=150, null=True, verbose_name='Creado por')),
                ('fe_us_in', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('us_mo', models.CharField(blank=True, max_length=150, null=True, verbose_name='Modificado por')),
                ('fe_us_mo', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('serial_cliente', models.CharField(help_text='Serial Cliente', max_length=3, primary_key=True, serialize=False, unique=True, verbose_name='Serial')),
                ('sello_dorado', models.BooleanField(default=False, help_text='Sello Dorado', verbose_name='Sello Dorado')),
                ('cedula', models.CharField(help_text='Cédula', max_length=12, verbose_name='Cédula')),
                ('nombre1', models.CharField(help_text='Nombre 1', max_length=20, verbose_name='Nombre 1')),
                ('nombre2', models.CharField(blank=True, help_text='Nombre 2', max_length=20, null=True, verbose_name='Nombre 2')),
                ('apellido1', models.CharField(help_text='Apellido 1', max_length=20, verbose_name='Apellido 1')),
                ('apellido2', models.CharField(blank=True, help_text='Apellido 2', max_length=20, null=True, verbose_name='Apellido 2')),
                ('urbanismo', models.CharField(help_text='Urbanismo', max_length=120, verbose_name='Urbanismo')),
                ('torre', models.CharField(help_text='Torre', max_length=10, verbose_name='Torre')),
                ('piso', models.CharField(help_text='Piso', max_length=8, verbose_name='Piso')),
                ('apartamento', models.CharField(help_text='Apartamento', max_length=8, verbose_name='Apartamento')),
                ('monto_credito', models.DecimalField(decimal_places=8, help_text='Monto Crédito Hipotecario a Otorgar', max_digits=18, verbose_name='Monto Crédito')),
                ('precio_venta', models.DecimalField(decimal_places=8, help_text='Precio de Venta', max_digits=18, verbose_name='Precio Venta')),
                ('precio_venta_divisa', models.DecimalField(decimal_places=8, help_text='Precio de Venta en Divisa', max_digits=18, verbose_name='Precio Venta Divisa')),
                ('inicial', models.DecimalField(decimal_places=8, help_text='Inicial', max_digits=18, verbose_name='Inicial')),
                ('inicial_porcentaje', models.DecimalField(decimal_places=8, help_text='% Inicial', max_digits=18, verbose_name='% Inicial')),
                ('identificador', models.CharField(help_text='Identificado', max_length=3, verbose_name='Identificado')),
                ('denominara', models.CharField(help_text='Denominara', max_length=20, verbose_name='Denominara')),
                ('ciudadano_ciudadana', models.CharField(help_text='Ciudadano/Ciudadana', max_length=20, verbose_name='Ciudadano/Ciudadana')),
                ('anios', models.CharField(help_text='Años', max_length=4, verbose_name='Años')),
                ('meses', models.CharField(help_text='Meses', max_length=3, verbose_name='Meses')),
                ('cuota_mensual', models.DecimalField(decimal_places=8, help_text='Cuota Mensual', max_digits=18, verbose_name='Cuota Mensual')),
                ('cuota_mensual_divisa', models.DecimalField(decimal_places=8, help_text='Cuota Mensual Divisa', max_digits=18, verbose_name='Cuota Mensual Divisa')),
                ('flat', models.DecimalField(decimal_places=8, help_text='Flat Hipotecario', max_digits=18, verbose_name='Flat Hipotecario')),
                ('flat_divisa', models.DecimalField(decimal_places=8, help_text='Flat Hipotecario Divisa', max_digits=18, verbose_name='Flat Hipotecario Divisa')),
                ('cuota_financiera', models.DecimalField(decimal_places=8, help_text='Cuota Financiera', max_digits=18, verbose_name='Cuota Financiera')),
                ('cuota_financiera_divisa', models.DecimalField(decimal_places=8, help_text='Cuota Financiera Divisa', max_digits=18, verbose_name='Cuota Financiera Divisa')),
                ('fongar', models.DecimalField(decimal_places=8, help_text='Fongar', max_digits=18, verbose_name='Fongar')),
                ('fongar_divisa', models.DecimalField(decimal_places=8, help_text='Fongar Divisa', max_digits=18, verbose_name='Fongar Divisa')),
                ('expediente', models.CharField(blank=True, help_text='Expediente', max_length=50, null=True, verbose_name='Expediente')),
                ('contrato_nro', models.CharField(blank=True, help_text='Nro. Contrato', max_length=50, null=True, verbose_name='Nro. Contrato')),
            ],
            options={
                'verbose_name': 'Dato',
                'verbose_name_plural': 'Datos',
                'ordering': ['serial_cliente'],
            },
        ),
    ]

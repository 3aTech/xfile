# Generated by Django 5.1.5 on 2025-02-09 17:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('us_in', models.CharField(blank=True, max_length=150, null=True, verbose_name='Creado por')),
                ('fe_us_in', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('us_mo', models.CharField(blank=True, max_length=150, null=True, verbose_name='Modificado por')),
                ('fe_us_mo', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('id', models.AutoField(help_text='Código', primary_key=True, serialize=False, verbose_name='Código')),
                ('ambiente', models.CharField(help_text='Ambiente', max_length=60, verbose_name='Ambiente')),
            ],
            options={
                'verbose_name': 'Ambiente',
                'verbose_name_plural': 'Ambientes',
                'ordering': ['ambiente'],
            },
        ),
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('us_in', models.CharField(blank=True, max_length=150, null=True, verbose_name='Creado por')),
                ('fe_us_in', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('us_mo', models.CharField(blank=True, max_length=150, null=True, verbose_name='Modificado por')),
                ('fe_us_mo', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('serial_cliente', models.CharField(help_text='Serial Cliente', max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Serial')),
                ('expediente', models.CharField(blank=True, help_text='Expediente', max_length=50, null=True, verbose_name='Expediente')),
                ('contrato_nro', models.CharField(blank=True, help_text='Nro. Contrato', max_length=50, null=True, verbose_name='Nro. Contrato')),
                ('sello_dorado', models.BooleanField(default=False, help_text='Sello Dorado', verbose_name='Sello Dorado')),
                ('nro_dorado_oficio', models.CharField(blank=True, help_text='Número Sello Dorado u Oficio', max_length=20, null=True, verbose_name='Número Sello Dorado u Oficio')),
                ('cedula', models.CharField(help_text='Cédula', max_length=12, verbose_name='Cédula')),
                ('identificador', models.CharField(help_text='Identificado', max_length=3, verbose_name='Identificado')),
                ('denominara', models.CharField(help_text='Denominara', max_length=20, verbose_name='Denominara')),
                ('ciudadano_ciudadana', models.CharField(help_text='Ciudadano/Ciudadana', max_length=20, verbose_name='Ciudadano/Ciudadana')),
                ('nombre1', models.CharField(help_text='Nombre 1', max_length=20, verbose_name='Nombre 1')),
                ('nombre2', models.CharField(blank=True, help_text='Nombre 2', max_length=20, null=True, verbose_name='Nombre 2')),
                ('apellido1', models.CharField(help_text='Apellido 1', max_length=20, verbose_name='Apellido 1')),
                ('apellido2', models.CharField(blank=True, help_text='Apellido 2', max_length=20, null=True, verbose_name='Apellido 2')),
                ('urbanismo', models.CharField(help_text='Urbanismo', max_length=120, verbose_name='Urbanismo')),
                ('torre', models.CharField(help_text='Torre', max_length=10, verbose_name='Torre')),
                ('piso', models.CharField(help_text='Piso', max_length=8, verbose_name='Piso')),
                ('apartamento', models.CharField(help_text='Apartamento', max_length=8, verbose_name='Apartamento')),
                ('metros_cuadrados', models.DecimalField(decimal_places=2, help_text='Mtrs2', max_digits=18, verbose_name='Mtrs2')),
                ('lindero_norte', models.CharField(blank=True, help_text='Lindero Norte', max_length=20, null=True, verbose_name='Lindero Norte')),
                ('lindero_sur', models.CharField(blank=True, help_text='Lindero Sur', max_length=20, null=True, verbose_name='Lindero Sur')),
                ('lindero_este', models.CharField(blank=True, help_text='Lindero Este', max_length=20, null=True, verbose_name='Lindero Este')),
                ('lindero_oeste', models.CharField(blank=True, help_text='Lindero Oeste', max_length=20, null=True, verbose_name='Lindero Oeste')),
                ('ambientes', models.CharField(blank=True, help_text='Datos de Ambientes', max_length=300, null=True, verbose_name='Datos de Ambientes')),
                ('monto_credito', models.DecimalField(decimal_places=8, help_text='Monto Crédito Hipotecario a Otorgar', max_digits=18, verbose_name='Monto Crédito')),
                ('precio_venta', models.DecimalField(decimal_places=8, help_text='Precio de Venta', max_digits=18, verbose_name='Precio Venta')),
                ('precio_venta_divisa', models.DecimalField(decimal_places=8, help_text='Precio de Venta en Divisa', max_digits=18, verbose_name='Precio Venta Divisa')),
                ('inicial', models.DecimalField(decimal_places=8, help_text='Inicial', max_digits=18, verbose_name='Inicial')),
                ('inicial_divisa', models.DecimalField(decimal_places=8, help_text='Inicial Divisa', max_digits=18, verbose_name='Inicial Divisa')),
                ('inicial_porcentaje', models.DecimalField(decimal_places=8, help_text='% Inicial', max_digits=18, verbose_name='% Inicial')),
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
            ],
            options={
                'verbose_name': 'Dato',
                'verbose_name_plural': 'Datos',
                'ordering': ['serial_cliente'],
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('us_in', models.CharField(blank=True, max_length=150, null=True, verbose_name='Creado por')),
                ('fe_us_in', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('us_mo', models.CharField(blank=True, max_length=150, null=True, verbose_name='Modificado por')),
                ('fe_us_mo', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('co_estado', models.CharField(help_text='Código del estado', max_length=6, primary_key=True, serialize=False, verbose_name='Código')),
                ('des_estado', models.CharField(help_text='Nombre del estado', max_length=60, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'ordering': ['des_estado'],
            },
        ),
        migrations.CreateModel(
            name='Lindero',
            fields=[
                ('us_in', models.CharField(blank=True, max_length=150, null=True, verbose_name='Creado por')),
                ('fe_us_in', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('us_mo', models.CharField(blank=True, max_length=150, null=True, verbose_name='Modificado por')),
                ('fe_us_mo', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('id', models.AutoField(help_text='Código', primary_key=True, serialize=False, verbose_name='Código')),
                ('lindero', models.CharField(help_text='Lindero', max_length=255, verbose_name='Lindero')),
            ],
            options={
                'verbose_name': 'Lindero',
                'verbose_name_plural': 'Linderos',
                'ordering': ['lindero'],
            },
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('us_in', models.CharField(blank=True, max_length=150, null=True, verbose_name='Creado por')),
                ('fe_us_in', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('us_mo', models.CharField(blank=True, max_length=150, null=True, verbose_name='Modificado por')),
                ('fe_us_mo', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('cedula', models.CharField(help_text='Cédula del representante', max_length=12, primary_key=True, serialize=False, verbose_name='Cédula')),
                ('nacionalidad', models.CharField(help_text='Nacionalidad', max_length=120, verbose_name='Nacionalidad')),
                ('nombre', models.CharField(help_text='Nombre y apellido del representante', max_length=120, verbose_name='Nombre y Apellido')),
                ('representante', models.CharField(help_text='Representante de', max_length=120, verbose_name='Representante de')),
                ('condicion', models.CharField(help_text='Condición y/o Caracter Representativo', max_length=120, verbose_name='Condición y/o Caracter Representativo')),
                ('inactivo', models.BooleanField(default=True, help_text='Estado de actividad', verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Representante',
                'verbose_name_plural': 'Representantes',
                'ordering': ['cedula', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Ambiente_Dato',
            fields=[
                ('us_in', models.CharField(blank=True, max_length=150, null=True, verbose_name='Creado por')),
                ('fe_us_in', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('us_mo', models.CharField(blank=True, max_length=150, null=True, verbose_name='Modificado por')),
                ('fe_us_mo', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('id', models.AutoField(help_text='Código', primary_key=True, serialize=False, verbose_name='Código')),
                ('id_ambiente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Ambiente_Dato', to='formulario.ambiente')),
                ('serial_cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ambiente_datos', to='formulario.datos')),
            ],
            options={
                'verbose_name': 'Ambiente Dato',
                'verbose_name_plural': 'Ambientes Datos',
                'ordering': ['serial_cliente'],
            },
        ),
        migrations.AddField(
            model_name='datos',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='datos', to='formulario.estado'),
        ),
        migrations.CreateModel(
            name='Lindero_Dato',
            fields=[
                ('us_in', models.CharField(blank=True, max_length=150, null=True, verbose_name='Creado por')),
                ('fe_us_in', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('us_mo', models.CharField(blank=True, max_length=150, null=True, verbose_name='Modificado por')),
                ('fe_us_mo', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('id', models.AutoField(help_text='Código', primary_key=True, serialize=False, verbose_name='Código')),
                ('id_lindero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Lindero_Dato', to='formulario.lindero')),
                ('serial_cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lindero_datos', to='formulario.datos')),
            ],
            options={
                'verbose_name': 'Lindero Dato',
                'verbose_name_plural': 'Linderos Datos',
                'ordering': ['serial_cliente'],
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('us_in', models.CharField(blank=True, max_length=150, null=True, verbose_name='Creado por')),
                ('fe_us_in', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('us_mo', models.CharField(blank=True, max_length=150, null=True, verbose_name='Modificado por')),
                ('fe_us_mo', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('co_municipio', models.CharField(help_text='Código del municipio', max_length=6, primary_key=True, serialize=False, verbose_name='Código')),
                ('des_municipio', models.CharField(help_text='Nombre del municipio', max_length=60, verbose_name='Nombre')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='municipios', to='formulario.estado')),
            ],
            options={
                'verbose_name': 'Municipio',
                'verbose_name_plural': 'Municipios',
                'ordering': ['des_municipio'],
            },
        ),
        migrations.AddField(
            model_name='datos',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='datos', to='formulario.municipio'),
        ),
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('us_in', models.CharField(blank=True, max_length=150, null=True, verbose_name='Creado por')),
                ('fe_us_in', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('us_mo', models.CharField(blank=True, max_length=150, null=True, verbose_name='Modificado por')),
                ('fe_us_mo', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('co_parroquia', models.CharField(help_text='Código de la parroquia', max_length=6, primary_key=True, serialize=False, verbose_name='Código')),
                ('des_parroquia', models.CharField(help_text='Nombre de la parroquia', max_length=60, verbose_name='Nombre')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='parroquias', to='formulario.municipio')),
            ],
            options={
                'verbose_name': 'Parroquia',
                'verbose_name_plural': 'Parroquias',
                'ordering': ['des_parroquia'],
            },
        ),
        migrations.AddField(
            model_name='datos',
            name='parroquia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='datos', to='formulario.parroquia'),
        ),
        migrations.AddField(
            model_name='datos',
            name='representante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='datos', to='formulario.representante'),
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('us_in', models.CharField(blank=True, max_length=150, null=True, verbose_name='Creado por')),
                ('fe_us_in', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('us_mo', models.CharField(blank=True, max_length=150, null=True, verbose_name='Modificado por')),
                ('fe_us_mo', models.DateTimeField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('co_sector', models.CharField(help_text='Código del sector', max_length=6, primary_key=True, serialize=False, verbose_name='Código')),
                ('des_sector', models.CharField(help_text='Nombre del sector', max_length=60, verbose_name='Nombre')),
                ('parroquia', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sectores', to='formulario.parroquia')),
            ],
            options={
                'verbose_name': 'Sector',
                'verbose_name_plural': 'Sectores',
                'ordering': ['des_sector'],
            },
        ),
        migrations.AddField(
            model_name='datos',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='datos', to='formulario.sector'),
        ),
    ]

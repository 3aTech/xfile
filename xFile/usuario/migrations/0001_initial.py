# Generated by Django 5.1.5 on 2025-02-25 13:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(default='users/usuario_defecto.jpg', help_text='Imagen', upload_to='users/', verbose_name='Foto de perfil')),
                ('address', models.CharField(blank=True, default='', help_text='Dirección', max_length=150, null=True, verbose_name='Dirección')),
                ('location', models.CharField(blank=True, default='', help_text='Localidad', max_length=150, null=True, verbose_name='Localidad')),
                ('phone', models.CharField(blank=True, default='', help_text='Teléfono', max_length=45, null=True, verbose_name='Teléfono')),
                ('created_by_admin', models.BooleanField(blank=True, default=True, help_text='Creado por el Administrador', null=True, verbose_name='Creador por Administradores')),
                ('us_windows', models.CharField(blank=True, default='', help_text='Conectado desde', max_length=20, null=True, verbose_name='Equipo')),
                ('online', models.BooleanField(blank=True, default=False, help_text='Online', null=True, verbose_name='Online')),
                ('dat_ult_fa', models.DateField(blank=True, help_text='Ultimo intento fellido', null=True)),
                ('dat_prox', models.DateField(blank=True, help_text='Proxímo cambio de contraseña', null=True)),
                ('veces', models.IntegerField(blank=True, default=0, help_text='Cantidad de sesiones erroneas', null=True)),
                ('co_us_in', models.CharField(blank=True, default=None, help_text='Código de usuario que registró', max_length=6, null=True, verbose_name='Credo por')),
                ('co_us_mo', models.CharField(blank=True, default=None, help_text='Código de usuario que modificó', max_length=6, null=True, verbose_name='Modificado por')),
                ('fe_us_mo', models.DateField(auto_now=True, help_text='Fecha que se modificó', null=True, verbose_name='Fecha de Modificación')),
                ('user', models.OneToOneField(help_text='login', on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfiles',
                'ordering': ['-id'],
            },
        ),
    ]

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

import datetime
dataNow = datetime.datetime.now().strftime('%Y-%m-%d')


# Perfil de Usuario

class Profile(models.Model):
    user:str = models.OneToOneField(User, on_delete=models.CASCADE, help_text='login', related_name='profile', verbose_name='Usuario') 
    picture = models.ImageField(default='users/usuario_defecto.jpg', upload_to='users/', help_text='Imagen', verbose_name='Foto de perfil')
    address:str = models.CharField(default='', help_text='Dirección', max_length=150, null=True, blank=True, verbose_name='Dirección')
    location:str = models.CharField(default='', help_text='Localidad', max_length=150, null=True, blank=True, verbose_name='Localidad')
    phone:str = models.CharField(default='', help_text='Teléfono', max_length=45, null=True, blank=True, verbose_name='Teléfono')
    created_by_admin:bool = models.BooleanField(default=True, help_text='Creado por el Administrador', null=True, blank=True, verbose_name='Creador por Administradores')
    us_windows:str = models.CharField(default='', help_text='Conectado desde', max_length=20, null=True, blank=True, verbose_name='Equipo')
    online:bool = models.BooleanField(default=False, help_text='Online', null=True, blank=True, verbose_name='Online')
    dat_ult_fa = models.DateField(help_text='Ultimo intento fellido', null= True, blank=True)
    dat_prox = models.DateField(help_text='Proxímo cambio de contraseña', null= True, blank=True)
    veces:int = models.IntegerField(help_text='Cantidad de sesiones erroneas', default= 0, null= True, blank=True)
    co_us_in:str = models.CharField('Credo por', help_text='Código de usuario que registró', default=None, max_length=6, null=True, blank=True)
    co_us_mo:str = models.CharField('Modificado por', help_text='Código de usuario que modificó', default=None, max_length=6, null=True, blank=True)
    fe_us_mo = models.DateField('Fecha de Modificación', help_text='Fecha que se modificó', null= True, blank=True, auto_now=True)


    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'
        ordering = ['-id']

    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile,sender=User)
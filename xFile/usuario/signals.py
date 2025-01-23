from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

@receiver(post_save, sender=Profile)
def add_user_to_group(sender, instance, created, **kwargs):
    if created:
        try:
            group1 = Group.objects.get(name='USUARIO')
        except Group.DoesNotExist:
            # Roles básicos
            group1 = Group.objects.create(name='USUARIO')    # Acceso limitado, solo lectura
            
            # Roles operativos
            group2 = Group.objects.create(name='USUARIO CMG')
            group3 = Group.objects.create(name='COORDINADOR')
            
            # Roles administrativos
            group4 = Group.objects.create(name='ASISTENTE ADMINISTRATIVO')    # Gestión financiera/administrativa
            
            # Roles técnicos
            group5 = Group.objects.create(name='ADMINISTRADOR')          # Acceso total al sistema
            
            # Rol máximo
            group6 = Group.objects.create(name='MASTER')       # Control total
            
        instance.user.groups.add(group1)
        
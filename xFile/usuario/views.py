from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib import messages
from .serializers import UserRegisterSerializer, UserLoginSerializer
from django.contrib.auth import login as auth_login
from rest_framework import serializers
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import get_user_permissions

def home(request):
    """Vista de Inicio"""
    context = {
        'perms': get_user_permissions(request.user)
    }
    return render(request, 'pages/list_datos.html', context)


# Create your views here.
def test(request):
    """Vista de Inicio"""
    context = {
        'perms': get_user_permissions(request.user)
    }
    return render(request, 'layouts/layouts-without-menu.html', context)

class RegisterView(APIView):
    def get(self, request):
        return render(request, 'accounts/register.html')
    
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, "Usuario creado exitosamente")
            #time.sleep(6)
            return redirect('login')
        else:
            for error in serializer.errors.values():
                messages.error(request, error[0])
            return render(request, 'accounts/register.html')

class LoginView(APIView):
    def get(self, request):
        return render(request, 'accounts/login.html')
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            auth_login(request, user)
            messages.success(request, "Inicio de sesión exitoso")
            return redirect('home')
        except serializers.ValidationError as e:
            # Manejo específico para diferentes tipos de errores
            if 'non_field_errors' in e.detail:
                messages.error(request, e.detail['non_field_errors'][0])
            else:
                for field, errors in e.detail.items():
                    messages.error(request, f"{field}: {errors[0]}")
            return render(request, 'accounts/login.html')

class SignOutView(LoginRequiredMixin, APIView):
    """
    Vista para cerrar sesión de usuario
    LoginRequiredMixin asegura que solo usuarios autenticados puedan acceder
    """
    def get(self, request):
        logout(request)
        messages.success(request, "Has cerrado sesión exitosamente")
        return redirect('home')

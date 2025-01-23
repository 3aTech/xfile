from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import authenticate

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user 

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        error_messages={
            'required': 'El nombre de usuario es requerido',
            'blank': 'El nombre de usuario no puede estar vacío'
        }
    )
    password = serializers.CharField(
        style={'input_type': 'password'}, 
        write_only=True,
        error_messages={
            'required': 'La contraseña es requerida',
            'blank': 'La contraseña no puede estar vacía'
        }
    )

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise serializers.ValidationError({
                        'non_field_errors': ['Tu cuenta está desactivada']
                    })
            else:
                raise serializers.ValidationError({
                    'non_field_errors': ['Usuario o contraseña incorrectos']
                })
        else:
            raise serializers.ValidationError({
                'non_field_errors': ['Debes proporcionar usuario y contraseña']
            })
        
        return data
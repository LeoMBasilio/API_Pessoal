from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError('Credenciais inválidas')

        refresh = RefreshToken.for_user(user)
        data['access'] = str(refresh.access_token)
        data['refresh'] = str(refresh)
        return data


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    is_staff = serializers.BooleanField(required=False)
    is_superuser = serializers.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_staff', 'is_superuser']
        read_only_fields = ['id']

    def validate(self, data):
        request = self.context.get('request')
        if request and not request.user.is_superuser:
            data.pop('is_staff', None)
            data.pop('is_superuser', None)
        return data

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user



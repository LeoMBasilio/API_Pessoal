from rest_framework import status, viewsets, permissions, mixins
from rest_framework.response import Response

from .models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer


class RegisterViewSet(viewsets.GenericViewSet):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Usuário criado"}, status=status.HTTP_201_CREATED)


class LoginViewSet(viewsets.GenericViewSet):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            "access": serializer.validated_data['access'],
            "refresh": serializer.validated_data['refresh'],
        }, status=status.HTTP_200_OK)


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return getattr(obj, 'usuario', None) == request.user


class IsSelfOrSuperuser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_superuser


class IsSuperuser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.IsAuthenticated(), IsSuperuser()]
        return [permissions.IsAuthenticated(), IsSelfOrSuperuser()]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.filter(pk=self.request.user.pk)


class SuperuserViewSet(viewsets.GenericViewSet):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperuser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_superuser(**serializer.validated_data)
        return Response({"msg": "Superuser criado"}, status=status.HTTP_201_CREATED)



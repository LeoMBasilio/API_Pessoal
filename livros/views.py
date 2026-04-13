from rest_framework import permissions, viewsets

from .models import Livro
from .serializers import LivroSerializer


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.usuario == request.user


class LivroViewSet(viewsets.ModelViewSet):
    serializer_class = LivroSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Livro.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

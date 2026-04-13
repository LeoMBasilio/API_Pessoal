from rest_framework import serializers

from .models import Livro


class LivroSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Livro
        fields = ['id', 'titulo', 'autor', 'publicado_em', 'status', 'url', 'usuario']

    def validate_status(self, value):
        if value not in ['nao lido', 'lendo', 'lido']:
            raise serializers.ValidationError("Status deve ser 'nao lido', 'lendo' ou 'lido'")
        return value

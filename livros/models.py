from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    publicado_em = models.DateField()
    status = models.CharField(max_length=20, default='nao lido')
    url = models.URLField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='livros')

    class Meta:
        db_table = 'custom_auth_livro'

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

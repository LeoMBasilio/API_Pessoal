from django.contrib import admin

from .models import Livro


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'publicado_em', 'status', 'usuario')
    list_filter = ('status', 'publicado_em')
    search_fields = ('titulo', 'autor', 'usuario__email')

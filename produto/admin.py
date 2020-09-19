from django.contrib import admin
from .models import Produto

# Register your models here.

class ProdutoAdmin( admin.ModelAdmin ):
    list_display = ('nome_produto','descricao_produto','custo','preco')
    list_display_links = ('nome_produto',)
    list_per_page = 20

admin.site.register(Produto,ProdutoAdmin)
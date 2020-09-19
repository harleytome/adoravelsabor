from django.db import models

# Create your models here.

class Produto(models.Model):
    nome_produto = models.CharField(max_length=200,verbose_name="Nome do Produto",blank=False)
    descricao_produto = models.TextField(verbose_name="Descrição",blank=False)
    custo = models.FloatField(verbose_name="Custo")
    preco = models.FloatField(verbose_name="Preço")

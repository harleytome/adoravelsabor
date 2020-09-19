from django.db import models

# Create your models here.
class Pedido( models.Model ):
    data_pedido = models.DateTimeField(verbose_name="Data do Pedido",blank=False)
    nome_cliente = models.CharField(max_length=255,verbose_name='Nome do Cliente',blank=False)
    data_entrega = models.DateTimeField(verbose_name="Data de Entrega",blank=False)
    forma_pagamento = models.CharField(
        max_length = 1,
        verbose_name="Formas de Pagamento",
        choices=(
                 ('D','Dinheiro'),
                 ('T','Transferência'),
                 ('P','PicPay')
                 )
    )
    pago = models.CharField(
        max_length = 1,
        verbose_name="Pago ?",
        choices=(
            ("S","Sim"),
            ("N","Não")
            )
    )
    entregue = models.CharField(
        max_length = 1,
        verbose_name="Entregue ?",
        choices=(
            ("S","Sim"),
            ("N","Não")
            )
    )

    def __str__(self):
        return f'Pedido Nr. {self.pk}'

class ItemPedido( models.Model ):
    pedido = models.ForeignKey(Pedido,on_delete = models.CASCADE)
    nome_produto = models.CharField(max_length=200,verbose_name="Nome do Produto",blank=False)
    quantidade = models.PositiveIntegerField(verbose_name="Quantidade",default=1)
    preco = models.FloatField(verbose_name="Preço")
    custo = models.FloatField(verbose_name="Custo")
    observacao = models.CharField(max_length=255,verbose_name="Observações",blank=True)

    def __str__(self):
        return f'Item do {self.pedido}'

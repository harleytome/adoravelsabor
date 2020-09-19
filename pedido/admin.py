from django.contrib import admin
from .models import Pedido,ItemPedido

# Register your models here.

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1

class PedidoAdmin( admin.ModelAdmin ):
    list_display = ('data_pedido','nome_cliente','data_entrega','forma_pagamento','pago','entregue')
    list_display_links = ('data_pedido','nome_cliente',)
    list_per_page = 20

    inlines = [
        ItemPedidoInline,
    ]
    

admin.site.register(Pedido,PedidoAdmin)
admin.site.register(ItemPedido)
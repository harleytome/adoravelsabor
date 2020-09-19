from django.urls import path
from . import views

app_name = "pedido"

urlpatterns = [
    #path('',views.index.as_view(),name='listaclientes'),
    path('novopedido/',views.NovoPedido.as_view(),name='novopedido'),
    path('novopedido/<int:pk>',views.PedidoSelCliente.as_view(),name='pedidoselcliente'),
    path('novopedido/adicionar/',views.AdicionaItemPedido,name='adicionaitem'),
    path('novopedido/del/<int:pk>',views.RemoveItemPedido,name='removeitem'),
]
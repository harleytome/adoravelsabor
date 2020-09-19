from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('',views.index.as_view(),name='listaprodutos'),
    path('cadastrar/',views.NovoProduto,name='novoproduto'),
    path('salvarproduto/',views.SalvarProduto,name='salvarproduto'),
    path('<int:pk>',views.AlterarProduto,name='alterarproduto'),
    path('salvaralteracao/',views.SalvarAlteracaoProduto,name='salvaralteracao'),
]
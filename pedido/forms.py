from django.forms import ModelForm
from django import forms
from cliente.models import Cliente
from produto.models import Produto
from .models import Pedido


class FormCliente(ModelForm):
      
    class Meta:
        model = Cliente
        fields = [
            'nome',
            'apelido',
            'telefone',
            'endereco',
            'numero',
            'complemento',
            'bairro',
            'cep',
            'cidade',
            'estado'
        ]

class FormProduto(ModelForm):

    nome_produto = forms.ModelChoiceField(
        queryset = Produto.objects.all(),
        to_field_name = 'id',
        initial = ''
    )
    class Meta:
        model = Produto
        fields = [
            'id',
            'nome_produto',
        ]

from django.forms import ModelForm
from django import forms
from .models import Cliente


class FormCliente(ModelForm):
      
    nome = forms.CharField(required=False,label="Nome *")
    telefone = forms.CharField(required=False, label="Telefone *")

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



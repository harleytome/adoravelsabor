from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from .models import Cliente
from .forms import FormCliente
from django.contrib import messages

from . import models
import pprint

# Create your views here.
class index(ListView):
    model = models.Cliente
    template_name = "cliente/index.html"
    context_object_name = "clientes"
    ordering = ["nome"]
    paginate_by = 10

class DetalheCliente(View):
    template_name = "cliente/detalhe.html"
    def setup(self, *args, **kwargs):
        super().setup(*args,**kwargs)
        # TODO : comentar
        print(".....................setup")
        self.pk = self.kwargs.get('pk')
        dados = get_object_or_404( Cliente,id=self.pk )
        self.contexto = {
                   'form': FormCliente( data=self.request.POST or None,instance=dados )
            }
        # TODO : apagar..não precisa
        #self.renderizar = render(self.request,self.template_name, self.contexto)

    def get(self, request, *args, **kwargs):
        # TODO : comentar
        print(".....................get")
        return render(request,self.template_name,self.contexto)
    
    def post(self,*args, **kwargs):
        # TODO : comentar
        print(".....................post")
        if self.request.POST['botao'] == "_cancelar_":
            return redirect('cliente:listaclientes')
        """
        Esta sendo enviado pelo form
        """
        #
        # dados do formulário serão recebidos no formato HTML
        #
        formulario = FormCliente(self.request.POST)
        if formulario.is_valid():
            #
            # o campo post será um objeto contendo os dados de cada campo do formulario
            # com os dados do Cliente (form)
            #
            nome = formulario.cleaned_data.get("nome")
            apelido = formulario.cleaned_data.get("apelido")
            telefone = formulario.cleaned_data.get("telefone")
            endereco = formulario.cleaned_data.get("endereco")
            numero = formulario.cleaned_data.get("numero")
            complemento = formulario.cleaned_data.get("complemento")
            bairro = formulario.cleaned_data.get("bairro")
            cep = formulario.cleaned_data.get("cep")
            cidade = formulario.cleaned_data.get("cidade")
            estado = formulario.cleaned_data.get("estado")

            if not nome:
                messages.error(self.request,"Nome é obrigatório")
                return render(self.request,self.template_name,self.contexto)
            
            if not telefone:
                messages.error(self.request,"O campo telefone é obrigatório")
                return render(self.request,self.template_name,self.contexto)
                
            cliente = get_object_or_404( Cliente,id=self.pk )
            cliente.nome = nome
            cliente.apelido = apelido
            cliente.telefone = telefone
            cliente.endereco = endereco
            cliente.numero = numero
            cliente.complemento = complemento
            cliente.bairro = bairro
            cliente.cep = cep
            cliente.cidade = cidade
            cliente.estado = estado
            cliente.save()

        return redirect('cliente:listaclientes') 


class NovoCliente(View):
    template_name = "cliente/novo.html"

    def setup(self, *args, **kwargs):
        super().setup(*args,**kwargs)
        # TODO : comentar
        print(".........setup Novo Cliente")
        self.contexto = {
                   'form': FormCliente( data=self.request.POST or None )
            }

    def get(self,request, *args, **kwargs):
        # TODO : remover
        print("..........get Novo Cliente")
        return render(request,self.template_name,self.contexto)

    def post(self,request,*args, **kwargs):
        # TODO : remover
        print("..........post Novo Cliente")
        if self.request.POST['botao'] == "_cancelar_":
            return redirect('cliente:listaclientes')
        
        formulario = FormCliente(self.request.POST)
        #formulario = self.contexto["form"]
        self.contexto = {
            "form" : formulario
        }

        if formulario.is_valid():
            nome = formulario.cleaned_data.get("nome")
            apelido = formulario.cleaned_data.get("apelido")
            telefone = formulario.cleaned_data.get("telefone")
            endereco = formulario.cleaned_data.get("endereco")
            numero = formulario.cleaned_data.get("numero")
            complemento = formulario.cleaned_data.get("complemento")
            bairro = formulario.cleaned_data.get("bairro")
            cep = formulario.cleaned_data.get("cep")
            cidade = formulario.cleaned_data.get("cidade")
            estado = formulario.cleaned_data.get("estado")

            if not nome:
                messages.error(self.request,"Nome é obrigatório")
                return render(self.request,self.template_name,self.contexto)
            
            if not telefone:
                messages.error(self.request,"O campo telefone é obrigatório")
                return render(self.request,self.template_name,self.contexto)

            cliente = Cliente (
                nome = nome,
                apelido = apelido,
                telefone = telefone,
                endereco = endereco,
                numero = numero,
                complemento = complemento,
                bairro = bairro,
                cep = cep,
                cidade = cidade,
                estado = estado
            )
            cliente.save()

        return redirect('cliente:listaclientes') 


        
    def clean_nome(self):
        nome = self.cleaned_data["nome"]
        print("OLA")
        if not nome:
            messages.error(self.request,"Nome é obrigatório")
        return nome



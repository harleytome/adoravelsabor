from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from .models import Produto
from django.contrib import messages
from django.db.models import F
import pprint

# Create your views here.

class index(ListView):
    #model = Produto
    template_name = "produto/listaprodutos.html"
    #context_object_name = "produtos"
    #ordering = ["nome"]
    paginate_by = 20

    def get(self,request,*args,**kwargs):
        p = Produto.objects.all().annotate(
            lucro  = F('preco')-F('custo')
        )
        c = {"produtos":p}
        return render(request, self.template_name, context=c)

def NovoProduto(request):
    template_name = "produto/novoproduto.html"
    contexto = {
        "prod" : Produto
    }  
    return render(request,template_name,contexto)

def SalvarProduto(request):
 
    template_name = "produto/novoproduto.html"
    nome_produto = request.POST.get("nome_produto")
    descricao_produto = request.POST.get("descricao_produto")
    custo = request.POST.get("custo")
    preco = request.POST.get("preco")

    if request.method == "POST":
        if request.POST['botao'] == "_cancelar_":
            return redirect('produto:listaprodutos')

        if not nome_produto:
            messages.error(request,"Nome do produto é obrigatório")
            return render(request,template_name,request.POST)
        if not descricao_produto:
            messages.error(request,"Descrição do produto é obrigatório")
            return render(request,template_name,request.POST)
        if not custo or not preco:
            messages.error(request,"Os valores precisam estar preenchidos")
            return render(request,template_name,request.POST)


    # converte os numeros formatados para float
    p = float(preco.replace('.','').replace(',','.'))
    c = float(custo.replace('.','').replace(',','.'))

    produto = Produto(
        nome_produto = nome_produto,
        descricao_produto = descricao_produto,
        custo = c,
        preco = p
    )
    produto.save()
    return redirect('produto:listaprodutos')

def AlterarProduto(request,pk):
    model = Produto
    template_name = "produto/alteraproduto.html"

    p = Produto.objects.get(
        id=pk
    )
    c = {"produto":p}
    return render(request, template_name, context=c)

def SalvarAlteracaoProduto(request):
    print(request.POST)
    if request.method == "POST":
        if request.POST['botao'] == "_cancelar_":
            return redirect('produto:listaprodutos')
    
    preco = (request.POST["preco"]).replace('.','').replace(',','.')
    custo = (request.POST["custo"]).replace('.','').replace(',','.')
    
    print("---------------->",preco," ",custo)
    pk = int(request.POST["pk"])
    produto = get_object_or_404(Produto,id = pk)
    produto.nome_produto = request.POST["nome_produto"]
    produto.descricao_produto = request.POST["descricao_produto"]
    produto.preco = float(preco)
    produto.custo = float(custo)
    produto.save()
    return redirect('produto:listaprodutos')
    

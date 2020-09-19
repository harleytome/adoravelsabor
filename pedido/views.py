from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from cliente.models import Cliente
from produto.models import Produto
from .models import Pedido
from django.views import View
from utils.utils import moeda_BR
import pprint

# TODO : remover o form pois não irá usar
#from .forms import FormCliente,FormProduto 

# Create your views here.
class NovoPedido(ListView):
    model = Cliente
    template_name = "pedido/index.html"
    context_object_name = "clientes"
    ordering = ["nome"]
    paginate_by = 10    

    def render_to_response(self, context, **response_kwargs):
        """
        Return a response, using the `response_class` for this view, with a
        template rendered with the given context.
        Pass response_kwargs to the constructor of the response class.
        """
        response_kwargs.setdefault('content_type', self.content_type)
        if self.request.session.get("carrinho"):
            del self.request.session["carrinho"]

        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs
        )

class PedidoSelCliente(View):
    template_name = "pedido/dadospedido.html"
    total_pedido = 0

    def setup(self, *args, **kwargs):
        super().setup(*args,**kwargs)
        self.pk = self.kwargs.get('pk')
        dados_cliente = get_object_or_404( Cliente,id=self.pk )
        dados_produto = Produto.objects.all()
        if self.request.session.get("carrinho"):
            for a,b in self.request.session["carrinho"].items():
                self.total_pedido += b["total_item"]
        print("------ total ----- ",self.total_pedido)
        self.contexto = {
                'cliente': dados_cliente,
                'produtos' : dados_produto,
                'carrinho' : self.request.session.get('carrinho'),
                'total_pedido' : self.total_pedido
            }      

    def get(self, request, *args, **kwargs):                
        return render(request,self.template_name,self.contexto)
        
 
def AdicionaItemPedido(request):

    id_cliente = request.POST.get("id_cliente")
    desc_produto = request.POST.get("desc_produto")
    observacao = request.POST.get("observacao")
    produto_selecionado = request.POST.get("produto_selecionado")
    preco_selecionado = request.POST.get("preco_selecionado")
    quantidade = request.POST.get("quantidade")

    """
    Inicio da sessão para guardar os dados
    """
    #del request.session["carrinho"]

    if not request.session.get("carrinho"): #verifica se a sessão de compras existe
        request.session["carrinho"] = {}
        request.session.save()
    
    carrinho = request.session["carrinho"]

    #carrinho["cliente"] = id_cliente 

    if produto_selecionado in carrinho: 
        carrinho[produto_selecionado]["cod_cliente"] = id_cliente
        carrinho[produto_selecionado]["desc_produto"] = desc_produto         
        carrinho[produto_selecionado]["produto"] = produto_selecionado
        carrinho[produto_selecionado]["observacao"] = observacao
        carrinho[produto_selecionado]["preco"] = float(moeda_BR(preco_selecionado))
        carrinho[produto_selecionado]["quantidade"] = int(quantidade)
        carrinho[produto_selecionado]["total_item"] = int(quantidade)*float(moeda_BR(preco_selecionado))
    else:
        carrinho[produto_selecionado] = {
            "cod_cliente" : id_cliente,
            "produto" : produto_selecionado,
            "observacao" : observacao,
            "preco" : float(moeda_BR(preco_selecionado)),
            "quantidade" : int(quantidade),
            "desc_produto" : desc_produto,
            "total_item" : int(quantidade)*float(moeda_BR(preco_selecionado))
        }
    request.session.save()
    
    # TODO : apagar
    print("----[ carrinho ]------------------------------------")
    pprint.pprint(carrinho)

    return redirect(
        reverse('pedido:pedidoselcliente',
        kwargs={
        'pk':id_cliente
    })
    )

def RemoveItemPedido(request,pk):
    del request.session["carrinho"][str(pk)]
    request.session.save()

    return redirect(
        reverse('pedido:pedidoselcliente',
        kwargs={
        'pk':pk
    })
    )    


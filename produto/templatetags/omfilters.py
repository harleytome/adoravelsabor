from django.template import Library
from utils import meusfiltros

register = Library()

@register.filter
def formata_preco(val):
    return meusfiltros.formata_preco(val)

@register.filter
def ajusta_centavos(num):
    return meusfiltros.ajusta_centavos(num)
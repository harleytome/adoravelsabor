"""
Será chamado em omfilters e registrado como filtros em templatetags
"""

def formata_preco(val):
    return f'R$ {val:.2f}'.replace('.',',')

def ajusta_centavos( num ):
    """
    ajusta a casa dos centavos quando fica com apenas um digito após a virgula
    """
    n = str(num) + "0"
    p = n.find(".")
    return f'R$ {n[0:p+3]}'.replace('.',',')


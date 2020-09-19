from django.db import models

# Create your models here.

class Cliente(models.Model):
    #nome = models.CharField(max_length=255,verbose_name='Nome',blank=True)
    nome = models.CharField(max_length=255,verbose_name='Nome',blank=False)
    apelido = models.CharField(max_length=255,verbose_name='Apelido/Referência',blank=True)
    #telefone = models.CharField(max_length=255,verbose_name='Telefone',blank=True)
    telefone = models.CharField(max_length=255,verbose_name='Telefone',blank=False)
    endereco = models.CharField(max_length=50,verbose_name='Endereço',blank=True)
    numero = models.CharField(max_length=5,verbose_name='Número',blank=True)
    complemento = models.CharField(max_length=40,blank=True,null=True,verbose_name='Complemento')
    bairro = models.CharField(max_length=30,verbose_name='Bairro',blank=True)
    cep = models.CharField(max_length=8,verbose_name='CEP',blank=True)
    cidade = models.CharField(max_length=30,verbose_name='Cidade',blank=True)
    estado = models.CharField(
        max_length=2,
        verbose_name='Estado',
        default='SP',
        choices=(
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantins'),
        )
    )


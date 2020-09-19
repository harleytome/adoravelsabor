from django.contrib import admin
from .models import Cliente

# Register your models here.

class ClienteAdmin( admin.ModelAdmin ):
    list_display = ('nome','apelido','telefone')
    list_display_links = ('nome',)
    list_per_page = 20

admin.site.register(Cliente,ClienteAdmin)

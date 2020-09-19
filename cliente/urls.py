from django.urls import path
from . import views

app_name = "cliente"

urlpatterns = [
    path('',views.index.as_view(),name='listaclientes'),
    path('cadastrar/',views.NovoCliente.as_view(),name='novocliente'),
    path('<int:pk>',views.DetalheCliente.as_view(),name='detalhecliente'),
]
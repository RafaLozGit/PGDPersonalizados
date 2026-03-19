from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('cliente/', views.cadastrar_cliente, name='cliente_list'),
    path('produto/', views.cadastrar_produto, name='produto_list'),
    path('pedido/', views.cadastrar_pedido, name='pedido_list'),
    path('excluir/<int:id>/', views.excluir_pedido, name='excluir'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('clientes/excluir/<int:id>/', views.excluir_cliente, name='excluir_cliente'),
    path('produtos/excluir/<int:id>/', views.excluir_produto, name='excluir_produto'),
]
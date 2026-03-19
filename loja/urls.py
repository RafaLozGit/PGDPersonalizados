from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('cliente/', views.cadastrar_cliente, name='cliente_list'),
    path('produto/', views.cadastrar_produto, name='produto_list'),
    path('pedido/', views.cadastrar_pedido, name='pedido_list'),
    path('excluir/<int:id>/', views.excluir_pedido, name='excluir'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cliente/', views.cadastrar_cliente, name='cliente'),
    path('produto/', views.cadastrar_produto, name='produto'),
    path('pedido/', views.cadastrar_pedido, name='pedido'),
    path('excluir/<int:id>/', views.excluir_pedido, name='excluir'),
]
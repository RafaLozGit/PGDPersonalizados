from django.shortcuts import render, redirect
from .models import Cliente, Produto, Pedido


def home(request):
    pedidos = Pedido.objects.all()
    return render(request, 'home.html', {'pedidos': pedidos})


def cadastrar_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')

        Cliente.objects.create(nome=nome, telefone=telefone)
        return redirect('home')

    return render(request, 'cadastrar_cliente.html')


def cadastrar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = float(request.POST.get('preco'))

        Produto.objects.create(nome=nome, preco=preco)
        return redirect('home')

    return render(request, 'cadastrar_produto.html')


def cadastrar_pedido(request):
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()

    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        produto_id = request.POST.get('produto')
        quantidade = int(request.POST.get('quantidade'))

        produto = Produto.objects.get(id=produto_id)
        total = produto.preco * quantidade

        Pedido.objects.create(
            cliente_id=cliente_id,
            produto_id=produto_id,
            quantidade=quantidade,
            total=total
        )

        return redirect('home')

    return render(request, 'cadastrar_pedido.html', {
        'clientes': clientes,
        'produtos': produtos
    })


def excluir_pedido(request, id):
    pedido = Pedido.objects.get(id=id)
    pedido.delete()
    return redirect('home')
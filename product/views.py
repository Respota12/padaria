from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm
from django.contrib import messages

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'product/listar.html', {'produtos': produtos})

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('inicial')
        else:
            messages.error(request, 'Erro ao cadastrar produto.')
    else:
        form = ProdutoForm()
    return render(request, 'product/cadastrar.html', {'form': form})
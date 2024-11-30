from django.contrib.auth import authenticate, logout, login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def cadastrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, "Usuário cadastrado com sucesso!")
            return redirect('login')  
        else:
            messages.error(request, "Erro ao cadastrar usuário.")
    else:
        form = UserCreationForm()
    
    return render(request, 'user/cadastrar.html', {'form': form})

def logar(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('inicial')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    return render(request, 'user/login.html')

@login_required
def inicial(request):
    return render(request, 'user/inicial.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logout realizado com sucesso!")
    return redirect('login')

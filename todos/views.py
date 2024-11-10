from django.shortcuts import render
from .models import Todo


# Create your views here.
def todo_list(request):
    todos = Todo.objects.all()

    # Passando 'nome' como contexto para o template
    return render(request, "todos/todo_list.html", {"todos": todos})

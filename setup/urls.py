from django.contrib import admin
from django.urls import path
from pathlib import Path

# Importação da view da aplicação 'todos'
from todos.views import todo_list

# Definição das URLs do projeto
urlpatterns = [
    path("admin/", admin.site.urls),  # URL para acessar o admin do Django
    path(
        "", todo_list, name="todo_list"
    ),  # URL raiz para a lista de todos, com nome nomeado
]

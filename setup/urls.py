from django.contrib import admin
from django.urls import path, include
from pathlib import Path
from todos.views import todo_list
from user.views import cadastrar, login, inicial
from django.urls import path
from todos.views import (
    TodoListView, 
    TodoCreateView, 
    TodoUpdateView, 
    TodoDeleteView, 
    TodoCompleteView,
)

# Definição das URLs do projeto
urlpatterns = [
    path("admin/", admin.site.urls),  # URL para acessar o admin do Django
    path("todo", TodoListView.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),
    path("cadastrar/", cadastrar, name="cadastrar"),
    path("login/", login, name="login"),
    path("", inicial, name="inicial")
]

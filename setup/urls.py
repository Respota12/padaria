from django.contrib import admin
from django.urls import path
from user.views import cadastrar, logar, inicial
from django.urls import path
from todos.views import (
    TodoListView, 
    TodoCreateView, 
    TodoUpdateView, 
    TodoDeleteView, 
    TodoCompleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("todo", TodoListView.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),
    path("cadastrar/", cadastrar, name="cadastrar"),
    path("login/", logar, name="login"),
    path("", inicial, name="inicial")
]

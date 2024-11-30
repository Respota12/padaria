from django.urls import path
from . import views

urlpatterns = [
    path("", views.cadastrar, name="cadastrar"),
    path("", views.logar, name="login"),
    path("", views.inicial, name="inicial")
]

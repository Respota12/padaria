from django.urls import path
from . import views

urlpatterns = [
    path("", views.cadastrar, name="cadastrar"),
    path("", views.login, name="login"),
    path("", views.inicial, name="inicial")
    
]

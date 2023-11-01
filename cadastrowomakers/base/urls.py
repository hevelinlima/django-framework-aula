from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("login/", views.login_view, name="login"),
]

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from base.forms import CadastroForm, LoginForm
from django.http import HttpResponse


def inicio(request):
    return render(request, "inicio.html")


def cadastro(request):
    if request.method == "POST":
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponse("Cadastrado")
    else:
        form = CadastroForm()
    return render(request, "cadastro.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponse(f"Logged in as {user.username}")
            else:
                return HttpResponse("Invalid login credentials")
        else:
            print(form.errors)
            return HttpResponse("Invalid form data")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from base.forms import CadastroForm, LoginForm
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required



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



@login_required
def user_profile(request):
    # Get the logged-in user using request.user
    user = request.user
    return render(request, 'user_profile.html', {'user': user})

def user_logout(request):
    logout(request)
    return redirect('base:login')  # Redirect to your login page or any other desired URL


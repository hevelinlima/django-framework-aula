from django import forms
from base.models import Cadastro
from django.contrib.auth.forms import AuthenticationForm


class CadastroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Cadastro
        fields = ("username", "email", "password")


class LoginForm(AuthenticationForm):
    class Meta:
        model = Cadastro
        fields = ("username", "password")

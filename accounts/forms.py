from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from . models import Profile
from intl_tel_input.widgets import IntlTelInputWidget

# If you don't do this you cannot use Bootstrap CSS


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Login", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'login', 'placeholder': 'Login', 'required': 'True', 'autofocus': 'True'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password', 'type': 'password', 'placeholder': 'Password', 'required': 'True'}))


class UserCreation(UserCreationForm):
    username = forms.CharField(label="", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'login', 'placeholder': 'Login', 'required': 'True', 'autofocus': 'True'}))
    first_name = forms.CharField(label="", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'Prenom', 'placeholder': 'Prénom', 'required': 'True', 'autofocus': 'True'}))
    last_name = forms.CharField(label="", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'Nom', 'placeholder': 'Nom', 'required': 'True', 'autofocus': 'True'}))
    numero_telephone = forms.CharField(label="", max_length=15, widget=IntlTelInputWidget(attrs={'required': 'True'}))
    email = forms.CharField(label="", max_length=30, widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'Email', 'placeholder': 'Email', 'required': 'True', 'autofocus': 'True'}))
    password1 = forms.CharField(label="", max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder': 'password', 'required': 'True', 'autofocus': 'True'}))
    password2 = forms.CharField(label="", max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password_validation', 'placeholder': 'password validation', 'required': 'True', 'autofocus': 'True'}))

    class Meta:
        model = Profile
        fields = ("username", "first_name", "last_name", "numero_telephone", "email", "password1", "password2")

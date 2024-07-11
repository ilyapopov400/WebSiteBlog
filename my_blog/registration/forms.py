from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    """
    Форма для регистрации пользователя
    """
    username = forms.CharField(label="ФИО", widget=forms.TextInput(attrs={"class": "form-input"}))
    email = forms.EmailField(label="email", widget=forms.EmailInput(attrs={"class": "form-input"}), required=False)
    password1 = forms.CharField(label="пароль", widget=forms.PasswordInput(attrs={"class": "form-input"}))
    password2 = forms.CharField(label="повтор пароля", widget=forms.PasswordInput(attrs={"class": "form-input"}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginUserForm(AuthenticationForm):
    """
    Форма для аутентификации пользователя
    """
    username = forms.CharField(label="логин", widget=forms.TextInput(attrs={"class": "form-input"}))
    password = forms.CharField(label="пароль", widget=forms.PasswordInput(attrs={"class": "form-input"}))

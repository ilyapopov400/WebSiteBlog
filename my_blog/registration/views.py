from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.urls import reverse_lazy


# Create your views here.

class LoginUser(LoginView):
    """
    Аутентификация пользователя
    """
    template_name = "registration/login.html"
    form_class = AuthenticationForm  # стандартная форма для аутентификации

    def get_success_url(self):
        return reverse_lazy("app_blog:index")


class LogoutUser(LogoutView):
    """
    Выход из идентификации пользователя
    """

    def get_success_url(self):
        return reverse_lazy("app_blog:index")

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy

from . import forms


# Create your views here.

class RegisterUser(CreateView):
    '''
    Страница регистрации в приложении
    '''
    # form_class = UserCreationForm  # стандартная форма для регистрации
    form_class = forms.RegisterUserForm  # собственная форма для регистрации
    template_name = "registration/register.html"
    success_url = reverse_lazy("registration:login")

    def form_valid(self, form):
        """
        При успешной регистрации автоматически проводим аутентификацию
        и переходим на главную страницу приложения
        :param form:
        :return:
        """
        user = form.save()
        login(self.request, user)
        return redirect("app_blog:index")


class LoginUser(LoginView):
    """
    Аутентификация пользователя
    """
    template_name = "registration/login.html"
    # form_class = AuthenticationForm  # стандартная форма для аутентификации
    form_class = forms.AuthenticationForm

    def get_success_url(self):
        return reverse_lazy("app_blog:index")


class LogoutUser(LogoutView):
    """
    Выход из идентификации пользователя
    """

    def get_success_url(self):
        return reverse_lazy("app_blog:index")

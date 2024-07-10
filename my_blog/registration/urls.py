from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name="login"),  # аутентификация пользователя

]

from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('registration/', views.RegisterUser.as_view(), name="registration"),  # регистрация пользователя
    path('login/', views.LoginUser.as_view(), name="login"),  # аутентификация пользователя
    path('logout/', views.LogoutUser.as_view(), name='logout'),  # выход из приложения
    path('delete/<int:pk>', views.DeleteUser.as_view(), name='delete_user'),  # удаление пользователя
]

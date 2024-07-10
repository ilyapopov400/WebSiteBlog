"""
Контекстные процессоры могут размещаться в любом месте кода,
но создание их в отдельном документе поможет вам лучше организовать структуру проекта
"""
from django.contrib.auth.models import User


def users(request):
    users_list = User.objects.all()
    return {'users_list': users_list}

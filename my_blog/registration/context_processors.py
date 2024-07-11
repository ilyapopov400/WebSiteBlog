"""
Контекстные процессоры могут размещаться в любом месте кода,
но создание их в отдельном документе поможет вам лучше организовать структуру проекта
"""
from django.contrib.auth.models import User


def users(request):
    """
    Передаем в контекст данные по пользователям (superuser - не передаем!)
    :param request:
    :return:
    """
    users_list = filter(lambda x: x.is_superuser is False, User.objects.all())
    return {'users_list': users_list}

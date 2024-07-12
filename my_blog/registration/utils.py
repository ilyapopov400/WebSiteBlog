"""
Необходимые утилиты
"""
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User


class OnlySuperuserMixin:
    """
    С помощью этого класса даем доступ только для 'superuser'
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseRedirect(reverse('registration:no_access_right'))
        return super().dispatch(request, *args, **kwargs)

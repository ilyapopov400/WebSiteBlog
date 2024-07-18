"""
Необходимые утилиты
"""
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from app_posts import models


class OnlySuperuserMixin:
    """
    С помощью этого класса даем доступ только для 'superuser'
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseRedirect(reverse('registration:no_access_right'))
        return super().dispatch(request, *args, **kwargs)


# class OnlySuperuserAndAuthorMixin:
#     """
#     С помощью этого класса даем доступ только для 'superuser' и автора поста
#     """
#
#     def dispatch(self, request, *args, **kwargs):
#         author = models.Posts.objects.all().get(pk=kwargs.get("pk"))
#
#         if request.user.is_superuser or request.user.pk == author.author.pk:
#             return super().dispatch(request, *args, **kwargs)
#         return HttpResponseRedirect(reverse('registration:no_access_right'))


# class OnlyAuthorMixin:  # TODO
#     """
#     С помощью этого класса даем доступ только для автора поста
#     """
#
#     def dispatch(self, request, *args, **kwargs):
#         author = models.Posts.objects.all().get(pk=kwargs.get("pk"))
#
#         if request.user.pk == request.user.pk == author.author.pk:
#             return super().dispatch(request, *args, **kwargs)
#         return HttpResponseRedirect(reverse('registration:no_access_right'))

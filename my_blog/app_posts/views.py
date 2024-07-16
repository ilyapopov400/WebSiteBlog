from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from . import models
from registration import utils


# Create your views here.

class PostsUser(DetailView):
    """
    - показать все посты пользователя
    """
    template_name = "app_posts/posts.html"
    model = User
    context_object_name = "authors"  # переменная, передающаяся в шаблон (можно использовать по дефолту object_list)

    def get_context_data(self, *args, **kwargs):
        """
        - добавили в контекст "posts_author" -> список постов выбранного автора
        :param args:
        :param kwargs:
        :return:
        """
        context = super().get_context_data(*args, **kwargs)
        posts_all = models.Posts.objects.all()
        posts_author = posts_all.filter(author=context.get("authors"))
        context["posts_author"] = posts_author
        return context


class PostUserOne(DetailView):
    """
    - показать один пост автора
    """
    template_name = "app_posts/post.html"
    model = models.Posts
    context_object_name = "post"


class PostUpdate(utils.OnlySuperuserAndAutorMixin, UpdateView):
    """
    - редактировать один пост
    - при использовании "utils.OnlySuperuserAndAutorMixin" разрешается только superuser и автору поста
    """
    template_name = "app_posts/update_post.html"
    model = models.Posts
    fields = ["title", "content"]

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('app_posts:posts_user_one', kwargs={'pk': pk})

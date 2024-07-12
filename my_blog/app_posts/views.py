from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView

from django.contrib.auth.models import User
from . import models


# Create your views here.

class PostsUser(DetailView):
    template_name = "app_posts/posts.html"
    model = User
    context_object_name = "authors"  # переменная, передающаяся в шаблон (можно использовать по дефолту object_list)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        posts_all = models.Posts.objects.all()
        posts_author = posts_all.filter(author=context.get("authors"))
        context["posts_author"] = posts_author
        return context

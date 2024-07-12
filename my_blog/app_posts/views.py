from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class PostsUser(TemplateView):
    template_name = "app_posts/posts.html"

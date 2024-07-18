from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

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


class PostCreate(CreateView):
    """
    - создать новый пост
    - при использовании "def dispatch()" доступ только автору страницы
    """
    template_name = "app_posts/create_post.html"
    model = models.Posts
    fields = ['title', 'content']

    # Функция для кастомной валидации полей формы модели
    def form_valid(self, form):
        fields = form.save(commit=False)
        # создаем форму, но не отправляем его в БД, пока просто держим в памяти
        # Через реквест передаем недостающую форму, которая обязательна
        fields.author = User.objects.get(pk=self.kwargs.get("pk"))
        # Наконец сохраняем в БД
        fields.save()
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        """
        - доступ только автору поста
        """
        author = self.kwargs.get("pk")

        if request.user.pk == author:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('registration:no_access_right'))

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('app_posts:posts_user', kwargs={'pk': pk})


class PostUserOne(DetailView):
    """
    - показать один пост автора
    """
    template_name = "app_posts/post.html"
    model = models.Posts
    context_object_name = "post"


class PostUpdate(UpdateView):
    """
    - редактировать один пост
    - при использовании "def dispatch()" разрешается только автору поста
    """
    template_name = "app_posts/update_post.html"
    model = models.Posts
    fields = ["title", "content"]

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('app_posts:posts_user_one', kwargs={'pk': pk})

    def dispatch(self, request, *args, **kwargs):
        """
        - доступ только автору поста
        """
        author = self.model.objects.all().get(pk=self.kwargs.get("pk")).author.pk

        if request.user.pk == author:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('registration:no_access_right'))


class PostDelete(utils.OnlySuperuserMixin, DeleteView):
    """
    - удалить пост
    - при использовании "utils.OnlySuperuserMixin" доступ только для "superuser"
    """
    template_name = "app_posts/delete_post.html"
    model = models.Posts
    success_url = reverse_lazy("app_posts:list_houses")

    def get_success_url(self):
        author = self.model.objects.all().get(pk=self.kwargs.get("pk")).author.pk
        return reverse_lazy('app_posts:posts_user', kwargs={'pk': author})

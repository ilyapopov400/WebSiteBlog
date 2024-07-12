from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


# Create your models here.

class Posts(models.Model):
    """
    Модель для хранения постов пользователей
    """
    title = models.CharField(max_length=20, verbose_name="заголовок поста",
                             validators=[MinLengthValidator(3)])  # заголовок поста
    content = models.TextField(verbose_name="содержимое поста", validators=[MinLengthValidator(3)], blank=True,
                               default="No content")  # содержимое поста
    date_create = models.DateTimeField(verbose_name="дата и время создания поста",
                                       auto_now_add=True)  # дата и время создания поста, устанавливается при создании
    date_change = models.DateTimeField(verbose_name="дата и время изменения поста",
                                       auto_now=True)  # дата и время изменения поста, изменяется при изменении
    autor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="автор поста")  # ссылка на модель User

    def __str__(self):
        return "{} - {}".format(self.autor, self.title)

    class Meta:
        verbose_name = 'пост пользователя'
        verbose_name_plural = 'посты пользователей'
        ordering = ["autor"]

    def get_absolute_url(self):
        return "/posts/{}/".format(self.pk)
        # return "/posts/%i/" % self.pk

from django.urls import path
from . import views

app_name = 'app_posts'

urlpatterns = [
    path('', views.PostsUser.as_view(), name="posts_user"),

]
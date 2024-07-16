from django.urls import path
from . import views

app_name = 'app_posts'

urlpatterns = [
    path('author/<int:pk>/', views.PostsUser.as_view(), name="posts_user"),  # все посты автора
    path('post/<int:pk>/', views.PostUserOne.as_view(), name="posts_user_one"),  # пост автора
    path('post_update/<int:pk>/', views.PostUpdate.as_view(), name="post_update"),  # редактирование поста

]

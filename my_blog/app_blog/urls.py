from django.urls import path
from . import views

app_name = 'app_blog'

urlpatterns = [
    path('', views.Index.as_view(), name="index"),

]

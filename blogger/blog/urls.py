# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # BlogPost CRUD operations
    path('posts', views.list_blog, name='list_blog'),
    path('create/', views.create_blog, name='create_blog'),
    path('delete_blog/<int:blog_id>/', views.delete_blog, name='delete_blog')
]

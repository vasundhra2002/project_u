from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user-list'),
    path('users/create/', views.user_create, name='create-user'),
    path('login/', views.login_view, name='login'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete-user')

]

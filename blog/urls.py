from django.urls import path
from .views import register, login_user, logout_user, home, post_detail, create_post, delete_post
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/create/', create_post, name='create_post'),
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'),
]

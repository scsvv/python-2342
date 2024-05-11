from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.all_posts, name='all_posts'),
    path('post/<int:post_id>', views.post_detail, name='post_detail'),
]
from django.urls import path
from myBlog.posts import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('posts/', views.list_posts, name='all_posts'),
    path('posts/<int:post_index>/', views.post_detail, name='post_detail'),
]

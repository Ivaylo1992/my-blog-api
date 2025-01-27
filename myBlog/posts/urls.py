from django.urls import path
from myBlog.posts import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('posts/', views.list_posts, name='all_posts'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('update/<int:post_id>/', views.update_post, name='post_update'),
    path('delete/<int:post_id>/', views.delete_post, name='post_delete'),
]

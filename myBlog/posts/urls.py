from django.urls import path
from myBlog.posts import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('posts/', views.PostListCreateView.as_view(), name='all_posts'),
    path('posts/<int:pk>/', views.PostRetrieveUpdateDeleteView.as_view(), name='post_retrieve_update_delete')
]

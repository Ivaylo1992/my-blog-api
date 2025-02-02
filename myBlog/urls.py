
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myBlog.posts.urls')),
    path('accounts/', include('myBlog.accounts.urls')),
]


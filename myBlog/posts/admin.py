from django.contrib import admin

from myBlog.posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...

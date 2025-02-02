from django.contrib import admin

from myBlog.posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    list_filter = ('created', )
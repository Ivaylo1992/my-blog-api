from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=50)

    content = models.TextField()

    created = models.DateTimeField(
        auto_now_add=True,
    )

    author = models.ForeignKey(
        to=UserModel, on_delete=models.CASCADE, related_name="posts"
    )

    def __str__(self) -> str:
        return self.title

from django.db import models
from django.contrib.auth.models import AbstractUser

from myBlog.accounts.managers import CustomUserManager

class User(AbstractUser):
    email = models.CharField(
        max_length=80,
        unique=True
    )

    username = models.CharField(
        max_length=50,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

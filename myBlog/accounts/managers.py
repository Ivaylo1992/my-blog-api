from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email=email)

        user = self.model(
            email=email,
            **extra_fields,
        )

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff set to True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser set to True")

        return self.create_user(email=email, password=password, **extra_fields)

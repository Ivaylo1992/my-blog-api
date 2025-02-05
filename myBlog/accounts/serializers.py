from rest_framework import serializers
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token

UserModel = get_user_model()


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    permission_classes = [AllowAny]

    class Meta:
        model = UserModel
        fields = ["email", "username", "password"]

    def validate(self, attrs):
        email_exists = UserModel.objects.filter(email=attrs["email"]).exists()

        if email_exists:
            raise ValidationError("Email has already been used")

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)

        user.set_password(password)

        user.save()

        Token.objects.create(user=user)

        return user


class CurrentUserPostsSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True,
        view_name="post_retrieve_update_delete",
        queryset=UserModel.objects.all(),
    )

    class Meta:
        model = UserModel
        fields = ["id", "username", "email", "posts"]

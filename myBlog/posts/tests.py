from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from myBlog.posts.views import PostListCreateView
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class HelloWordTest(APITestCase):
    def test_hello_world(self):
        response = self.client.get(reverse("home_page"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("message"), "Hello world!")


class PostListCreateTest(APITestCase):
    def setUp(self):
        self.url = reverse("all_posts")

    def authenticate(self):
        self.client.post(
            reverse("signup"),
            data={
                "email": "test@app.com",
                "password": "password123##",
                "username": "testUser",
            },
        )

        response = self.client.post(
            reverse("login"),
            data={"email": "test@app.com", "password": "password123##"},
        )

        token = response.data["tokens"]["access"]

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_list_post(self):

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)
        self.assertEqual(response.data["results"], [])

    def test_post_creation(self):
        self.authenticate()

        sample_data = {"title": "sample title", "content": "sample title"}

        response = self.client.post(self.url, sample_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data["title"], sample_data["title"])

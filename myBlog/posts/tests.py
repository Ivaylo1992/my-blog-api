from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from myBlog.posts.views import PostListCreateView
from django.contrib.auth import get_user_model


UserModel = get_user_model()

class HelloWordTest(APITestCase):
    def test_hello_world(self):
        response = self.client.get(reverse('home_page'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('message'), 'Hello world!')

        


class PostListCreateTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = PostListCreateView.as_view()
        self.url = reverse('all_posts')

        self.user = UserModel.objects.create(
            username='TestUser',
            email='test@user.com',
            password='password123'
        )
    
    def test_list_post(self):
        request = self.factory.get(self.url)

        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 0)
        self.assertEqual(response.data['results'], [])
        

    def test_post_creation(self):
        sample_post = {
            'title': 'sample title',
            'content': 'sample content'
        }


        request = self.factory.post(self.url, sample_post)
        request.user = self.user

        response = self.view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from myBlog.posts.models import Post
from myBlog.posts.serializers import PostSerializer
from rest_framework import generics as api_views
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

@api_view(['GET', 'POST'])
def home_page(request: Request):
    if request.method == 'POST':
        data = request.data

        response = {
            'message': 'Hello world!',
            'data': data,
        }

        return Response(data=response, status=status.HTTP_200_OK)
        

    response = {
        'message': 'Hello world!'
    }

    return Response(data=response, status=status.HTTP_200_OK)


class PostListCreateView(api_views.GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request:Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request:Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class PostRetrieveUpdateDeleteView(api_views.GenericAPIView,
        RetrieveModelMixin,
        UpdateModelMixin,
        DestroyModelMixin
):
    
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request:Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from myBlog.posts.models import Post
from myBlog.posts.serializers import PostSerializer
from rest_framework import generics as api_views
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from rest_framework.generics import GenericAPIView
from myBlog.accounts.serializers import CurrentUserPostsSerializer
from myBlog.posts.permissions import AuthorOrReadOnly
from drf_yasg.utils import swagger_auto_schema


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def home_page(request: Request):
    if request.method == "POST":
        data = request.data

        response = {
            "message": "Hello world!",
            "data": data,
        }

        return Response(data=response, status=status.HTTP_200_OK)

    response = {"message": "Hello world!"}

    return Response(data=response, status=status.HTTP_200_OK)


class PostListCreateView(api_views.GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

        return super().perform_create(serializer=serializer)

    @swagger_auto_schema(
        operation_summary='List all posts',
        operation_description='Returns list of all posts'
    )
    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Create a post',
        operation_description='Creates a post'
    )
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostRetrieveUpdateDeleteView(
    api_views.GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
):

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AuthorOrReadOnly]

    @swagger_auto_schema(
        operation_summary='Retrieve a post by id',
        operation_description='Retrieves a post by an id'
    )
    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Update a post by id',
        operation_description='Updates a post by an id'
    )
    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Delete a post by id',
        operation_description='Deletes a post by an id'
    )
    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ListPostsForAuthor(GenericAPIView, ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.request.query_params.get("username", None)

        if username is not None:
            return Post.objects.filter(author__username=username)

        return self.queryset.all()

    @swagger_auto_schema(
        operation_summary='Retrieve a post by a given user',
        operation_description='Retrieve a post by a given user'
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

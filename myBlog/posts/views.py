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
from myBlog.accounts.serializers import CurrentUserPostsSerializer
from myBlog.posts.permissions import ReadOnly, AuthorOrReadOnly


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
    permission_classes = [ReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

        return super().perform_create(serializer=serializer)

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostRetrieveUpdateDeleteView(
    api_views.GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
):

    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [AuthorOrReadOnly]

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_posts_for_current_user(request: Request):
    user = request.user
    serializer = CurrentUserPostsSerializer(instance=user, context={"request": request})

    return Response(data=serializer.data, status=status.HTTP_200_OK)

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from myBlog.posts.models import Post
from myBlog.posts.serializers import PostSerializer
from django.shortcuts import get_object_or_404

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


@api_view(['GET', 'POST'])
def list_posts(request:Request):
    posts = Post.objects.all()

    if request.method == 'POST':
        data = request.data

        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                'message': 'Post Created',
                'data': serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer = PostSerializer(instance=posts, many=True)

    response = {
        'message': 'posts',
        'data': serializer.data,
    }

    return Response(data=response, status=status.HTTP_200_OK)


@api_view(['GET'])
def post_detail(request:Request, post_id:int):
    post = get_object_or_404(Post, pk=post_id)

    serializer = PostSerializer(instance=post)

    response = {
        'message': 'post',
        'data': serializer.data
    }

    return Response(data=response, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_post(request:Request, post_id:int):
    post = get_object_or_404(Post, pk=post_id)

    data = request.data
    
    serializer = PostSerializer(instance=post, data=data)

    if serializer.is_valid():
        serializer.save()

        response = {
            'message': 'Post updated successfully',
            'data': serializer.data
        }
        
        return Response(data=response, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


@api_view(['DELETE'])
def delete_post(request:Request, post_id:int):
    post = get_object_or_404(Post, pk=post_id)
    
    post.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)
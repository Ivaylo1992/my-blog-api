from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

posts = [
    {
        'title': 'Post 1',
        'content': 'content 1',
        'author': 'author 1'
    },
    {
        'title': 'Post 2',
        'content': 'content 2',
        'author': 'author 2'
    },
    {
        'title': 'Post 3',
        'content': 'content 3',
        'author': 'author 3'
    }
]

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


@api_view(['GET'])
def list_posts(request:Request):
    return Response(data=posts, status=status.HTTP_200_OK)


@api_view(['GET'])
def post_detail(request:Request, post_index:int):
    post = posts[post_index]

    if post:
        return Response(data=post, status=status.HTTP_200_OK)
    
    return Response(
        data={"error": "Post not found"},
        status=status.HTTP_404_NOT_FOUND
    )
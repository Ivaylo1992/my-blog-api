from django.urls import path
from myBlog.accounts import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup')
]


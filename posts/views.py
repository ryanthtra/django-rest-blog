# posts/views.py
#from django.shortcuts import render # not rendering anything
from django.contrib.auth import get_user_model
from rest_framework import viewsets #generics, permissions

from . models import Post
from . serializers import PostSerializer, UserSerializer
from . permissions import IsAuthorOrReadOnly



# Create your views here.
# class PostList(generics.ListCreateAPIView):
#   # View-level permissions
#   # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#   queryset = Post.objects.all()
#   serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#   # View-level permissions
#   permission_classes = (IsAuthorOrReadOnly,) #(permissions.IsAuthenticated,)
#   queryset = Post.objects.all()
#   serializer_class = PostSerializer

# Replaces the two preceding classes
class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

# class UserList(generics.ListAPIView):
#   queryset = get_user_model().objects.all()
#   serializer_class = UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#   queryset = get_user_model().objects.all()
#   serializer_class = UserSerializer

# Replaces the two preceding classes
class UserViewSet(viewsets.ModelViewSet):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer
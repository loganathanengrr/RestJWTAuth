from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework import permissions
from .serializers import UserSerializer

User = User =  get_user_model() 

# Create your views here.

class RegisterUser(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListView(generics.ListAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

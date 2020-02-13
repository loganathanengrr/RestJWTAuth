from django.urls import path
from rest_framework_jwt.views import (
    obtain_jwt_token as create_token,
    refresh_jwt_token as refresh_token,
    verify_jwt_token as verify_token
)
from . import views

urlpatterns = [
    path('register_user', views.RegisterUser.as_view(), name='register_user'),
    path('users', views.UserListView.as_view(), name='users_list'),
    path('create_jwt_token', create_token, name='create_jwt_token'),
    path('refresh_jwt_token', refresh_token, name='refresh_jwt_token'),
    path('verify_jwt_token', verify_token, name='verify_jwt_token')
]
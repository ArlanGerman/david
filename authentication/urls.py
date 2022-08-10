from django.contrib import admin
from django.urls import path
from authentication.views import UserCreateAPIView

urlpatterns = [
    path('create/', UserCreateAPIView.as_view()),
]
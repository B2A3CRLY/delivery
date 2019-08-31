from django.urls import path, include
from .views import RegisterAPI, LoginAPI, UserAPI

urlpatterns = [
    path('auth/register', RegisterAPI.as_view()),
    path('auth/login', LoginAPI.as_view()),
    path('auth/user', UserAPI.as_view()),
]

from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import (
    UserSerializer, RegisterSerializer, LoginSerializer)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({
            "user": UserSerializer(
                user, context=self.get_serializer_context()).data,
            "token": token
        })


# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({
            "user": UserSerializer(
                user, context=self.get_serializer_context()).data,
            "token":  token
        })


# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = UserSerializer
    lookup_field = 'username'

    def get_object(self):
        return self.request.user

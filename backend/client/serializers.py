from backend.models import Client
from users.serializers import UserSerializer
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    created_by = UserSerializer (many = False,read_only=True)
    class Meta:
        model = Client
        fields = '__all__'


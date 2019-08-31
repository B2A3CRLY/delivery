from backend.models import Delivery
from backend.client.serializers import ClientSerializer
from backend.parcel.serializers import ParcelSerializer
from rest_framework import serializers


class DeliverySerializer(serializers.ModelSerializer):
    parcels = ParcelSerializer(many=True,read_only=True)

    class Meta:
        model = Delivery
        fields = '__all__'

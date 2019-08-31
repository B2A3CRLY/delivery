from backend.models import Parcel, Article
from backend.client.serializers import ClientSerializer
from backend.article.serializers import ArticleSerializer
from rest_framework import serializers


class ParcelSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)
    client = ClientSerializer(many=False, read_only=True)

    class Meta:
        model = Parcel
        fields = '__all__'

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from models_app.models import Photo


class PhotoShowDetailSerializer(ModelSerializer):
    author = serializers.CharField(source="author.username")
    publication_date = serializers.DateTimeField(format="%m-%d-%Y %H:%M")

    class Meta:
        model = Photo
        fields = [
            "id",
            "author",
            "title",
            "description",
            "publication_date",
            "image",
            "previous_image",
            "state",
        ]

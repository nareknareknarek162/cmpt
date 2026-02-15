from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from models_app.models import Photo


class PhotoCreateSerializer(ModelSerializer):
    author_id = serializers.IntegerField()
    image = serializers.ImageField()

    class Meta:
        model = Photo
        fields = [
            "author_id",
            "title",
            "description",
            "image",
        ]

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from models_app.models import Photo


class PhotoShowSerializer(ModelSerializer):
    image_preview = serializers.SerializerMethodField()

    class Meta:
        model = Photo
        fields = ["id", "image", "image_preview", "title", "description"]

    def get_image_preview(self, obj):
        if obj.image_preview:
            return obj.image_preview.url
        return None

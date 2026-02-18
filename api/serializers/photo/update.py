from rest_framework.serializers import ModelSerializer

from models_app.models import Photo


class PhotoUpdateSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            "title",
            "description",
            "image",
        ]

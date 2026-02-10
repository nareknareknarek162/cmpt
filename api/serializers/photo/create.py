from rest_framework.serializers import ModelSerializer

from models_app.models import Photo


class PhotoCreateSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            "id",
            "author",
            "title",
            "publication_date",
            "description",
            "image",
            "state",
        ]

from rest_framework.serializers import BooleanField, ModelSerializer

from models_app.models import Photo


class PhotoModifySerializer(ModelSerializer):
    restore = BooleanField(required=False, default=False)

    class Meta:
        model = Photo
        fields = ["title", "description", "image", "restore"]

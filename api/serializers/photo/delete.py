from rest_framework.serializers import ModelSerializer

from models_app.models import Photo


class PhotoDeleteSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ["id"]

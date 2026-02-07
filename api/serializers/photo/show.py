from rest_framework.serializers import ModelSerializer

from models_app.models import Photo


class PhotoShowSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ["id", "title"]

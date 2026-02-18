from rest_framework.serializers import ModelSerializer

from models_app.models import Photo


class PhotoShowDetailSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = ["author_id", "title", "description", "publication_date", "image", "state"]

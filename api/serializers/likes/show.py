from rest_framework.serializers import ModelSerializer

from models_app.models import Like


class LikeShowSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ["photo_id", "user"]

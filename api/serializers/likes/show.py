from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from models_app.models import Like


class LikeShowSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ["user"]


class LikesResponseSerializer(serializers.Serializer):
    liked = serializers.BooleanField()
    likes = LikeShowSerializer(many=True)

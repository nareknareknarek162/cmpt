from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from models_app.models import User


class UserShowSerializer(ModelSerializer):
    avatar_thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "avatar",
            "avatar_thumbnail",
        ]

    def get_avatar_thumbnail(self, obj):
        if obj.avatar_thumbnail:
            return obj.avatar_thumbnail.url
        return None

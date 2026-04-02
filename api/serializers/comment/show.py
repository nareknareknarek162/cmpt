from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from models_app.models import Comment


class CommentShowSerializer(ModelSerializer):
    author = serializers.CharField(source="author.username")
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Comment
        fields = [
            "id",
            "author",
            "text",
            "photo",
            "created_at",
            "updated_at",
            "parent_comment",
        ]

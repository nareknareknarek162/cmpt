from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from models_app.models import Comment


class CommentShowSerializer(ModelSerializer):
    author = serializers.CharField(source="author.username")
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M")
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M")
    children = serializers.SerializerMethodField()

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
            "children",
        ]

    def get_children(self, obj):
        return CommentShowSerializer(getattr(obj, "children_list", []), many=True).data


class CommentResponseSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    tree = CommentShowSerializer(many=True)

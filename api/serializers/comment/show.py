from rest_framework.serializers import ModelSerializer

from models_app.models import Comment


class CommentShowSerializer(ModelSerializer):
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

from rest_framework.serializers import ModelSerializer

from models_app.models import Comment


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "author", "text", "photo", "created_at"]

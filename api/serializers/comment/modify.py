from rest_framework.serializers import ModelSerializer

from models_app.models import Comment


class CommentModifySerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "text"]

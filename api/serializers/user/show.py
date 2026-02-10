from rest_framework.serializers import ModelSerializer

from models_app.models import User


class UserShowSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name"]

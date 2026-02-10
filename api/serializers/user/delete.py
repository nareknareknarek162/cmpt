from rest_framework.serializers import ModelSerializer

from models_app.models import User


class UserDeleteSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]

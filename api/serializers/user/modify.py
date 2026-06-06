from rest_framework.serializers import ModelSerializer

from models_app.models import User


class UserModifySerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "password",
            "gender",
            "avatar",
            "avatar_thumbnail",
        ]

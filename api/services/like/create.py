from django import forms
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Like, User


class LikeCreateService(ServiceWithResult):
    id = forms.IntegerField(required=True, min_value=1)
    user = ModelField(User)

    def process(self):
        self.result = self._create_like()
        return self

    def _create_like(self):
        like = Like.objects.create(
            user_id=self.cleaned_data["user"].id, photo_id=self.cleaned_data["id"]
        )

        return like

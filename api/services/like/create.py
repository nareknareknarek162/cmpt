from django import forms
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Like, User


class LikeCreateService(ServiceWithResult):
    photo_id = forms.IntegerField(required=True)
    user = ModelField(User)

    def process(self):
        self.result = self._create_like()
        return self

    def _create_like(self):
        like = Like.objects.create(
            user=self.cleaned_data["user"], photo_id=self.cleaned_data["photo_id"]
        )

        return like

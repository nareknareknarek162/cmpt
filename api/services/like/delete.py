from django import forms
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Like, User


class LikeDeleteService(ServiceWithResult):
    id = forms.IntegerField(required=True, min_value=1)
    user = ModelField(User)

    def process(self):
        self.result = self._delete_like()
        return self

    def _delete_like(self):
        like = Like.objects.filter(
            user_id=self.cleaned_data["user"].id, photo_id=self.cleaned_data["id"]
        )

        like.delete()
        return like

from django import forms
from service_objects.services import ServiceWithResult

from models_app.models import Like


class LikesShowService(ServiceWithResult):
    id = forms.IntegerField(required=True)

    def process(self):
        self.result = self._likes()
        return self

    def _likes(self):
        return Like.objects.filter(photo_id=self.cleaned_data["id"])

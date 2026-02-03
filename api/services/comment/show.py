from django import forms
from service_objects.services import ServiceWithResult

from models_app.models import Comment


class CommentShowService(ServiceWithResult):
    id = forms.IntegerField(min_value=1, required=True)

    def process(self):
        self.result = self._photo()
        return self

    def _photo(self):
        return Comment.objects.get(id=self.cleaned_data["id"])

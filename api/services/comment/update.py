from django import forms
from service_objects.services import ServiceWithResult

from models_app.models import Comment, User


class CommentUpdateService(ServiceWithResult):
    id = forms.IntegerField(required=True, min=1)
    text = forms.CharField()

    def process(self):
        self.result = self._update_photo()
        return self

    def _update_photo(self):
        pass
        # updating logic here

from django import forms
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Comment, User


class CommentCreateService(ServiceWithResult):
    photo = forms.IntegerField(required=True)
    author = ModelField(User)
    text = forms.CharField()
    created_at = forms.CharField()

    def process(self):
        self.result = self._create_photo()
        return self

    def _create_photo(self):
        comment = Comment.objects.create(
            author=self.cleaned_data["author"],
            photo=self.cleaned_data["photo"],
            text=self.cleaned_data["text"],
            created_at=self.cleaned_data["created_at"],
        )

        return comment

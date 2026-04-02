from django import forms
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Comment, User


class CommentCreateService(ServiceWithResult):
    id = forms.IntegerField(required=True, min_value=1)
    author = ModelField(User)
    text = forms.CharField(required=True)

    def process(self):
        self.result = self._create_comment()
        return self

    def _create_comment(self):
        comment = Comment.objects.create(
            author_id=self.cleaned_data["author"].id,
            photo_id=self.cleaned_data["id"],
            text=self.cleaned_data["text"],
        )

        return comment

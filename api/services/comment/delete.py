from django import forms
from django.core.exceptions import ObjectDoesNotExist
from service_objects.services import ServiceWithResult

from models_app.models import Comment


class CommentDeleteService(ServiceWithResult):
    id = forms.IntegerField(min_value=1, required=True)

    def process(self):
        self.result = self._delete_comment()
        return self

    def _delete_comment(self):
        try:
            comment = Comment.objects.get(id=self.cleaned_data["id"])
        except ObjectDoesNotExist:
            return None

        comment.delete()
        return comment

from django import forms
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework import status
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Comment, User


class CommentUpdateService(ServiceWithResult):
    id = forms.IntegerField(required=True, min_value=1)
    text = forms.CharField(required=True, min_length=1, max_length=127)
    user = ModelField(User)

    custom_validations = ["_validate_comment_exist", "_validate_author"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._update_comment()
        return self

    def _update_comment(self):
        comment = Comment.objects.get(id=self.cleaned_data["id"])
        comment.text = self.cleaned_data["text"]

        comment.save()
        return comment

    @property
    def _comment(self):
        try:
            return Comment.objects.get(id=self.cleaned_data["id"])
        except ObjectDoesNotExist:
            return None

    def _validate_comment_exist(self):
        if not self._comment:
            self.add_error(
                "id", ValidationError(message="Запрошенного комментария нет")
            )
            self.response_status = status.HTTP_404_NOT_FOUND

    def _validate_author(self):
        if self._comment and self.cleaned_data["user"].id != self._comment.author_id:
            self.add_error("id", ValidationError(message="Нет доступа"))
            self.response_status = status.HTTP_403_FORBIDDEN

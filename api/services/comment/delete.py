from functools import lru_cache

from django import forms
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework import status
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Comment, User


class CommentDeleteService(ServiceWithResult):
    id = forms.IntegerField(min_value=1, required=True)
    user = ModelField(User)

    custom_validations = ["_validate_comment_exists", "_validate_author"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._delete_comment()
        return self

    def _delete_comment(self):
        comment = self._comment

        comment.delete()
        return comment

    @property
    @lru_cache
    def _comment(self):
        try:
            return Comment.objects.get(id=self.cleaned_data["id"])
        except ObjectDoesNotExist:
            return None

    def _validate_comment_exists(self):
        if not self._comment:
            self.add_error(
                "id", ValidationError(message="Запрошенного комментария нет")
            )
            self.response_status = status.HTTP_404_NOT_FOUND

    def _validate_author(self):
        if self._comment and self.cleaned_data["user"].id != self._comment.author_id:
            self.add_error("id", ValidationError(message="Нет доступа"))
            self.response_status = status.HTTP_403_FORBIDDEN

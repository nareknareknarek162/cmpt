from functools import lru_cache

from django import forms
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework import status
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Comment, Photo, User


class CommentCreateService(ServiceWithResult):
    id = forms.IntegerField(required=True, min_value=1)
    author = ModelField(User)
    text = forms.CharField(required=True, min_length=2)
    parent_comment = forms.IntegerField(required=False, min_value=1)

    custom_validations = ["_validate_photo_exist"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._create_comment()
        return self

    def _create_comment(self):
        comment = Comment.objects.create(
            author_id=self.cleaned_data["author"].id,
            photo_id=self.cleaned_data["id"],
            text=self.cleaned_data["text"],
            parent_comment_id=self.cleaned_data.get("parent_comment"),
        )

        return comment

    @property
    @lru_cache
    def _photo(self):
        try:
            return Photo.objects.get(id=self.cleaned_data["id"])
        except ObjectDoesNotExist:
            return None

    def _validate_photo_exist(self):
        if not self._photo:
            self.add_error(
                "photo", ValidationError(message="Запрошенной фотографии не существует")
            )
            self.response_status = status.HTTP_404_NOT_FOUND

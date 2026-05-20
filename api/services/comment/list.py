from functools import lru_cache

from django import forms
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework import status
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Comment, Photo, User


class CommentShowListService(ServiceWithResult):
    id = forms.IntegerField(min_value=1, required=True)
    user = ModelField(User, required=False)

    custom_validations = ["_validate_photo_exist", "_validate_photo_approved"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._build_tree()
        return self

    def _comments(self):
        return Comment.objects.filter(photo=self.cleaned_data["id"])

    def _build_tree(self):
        comments = self._comments()
        by_id = {c.id: c for c in comments}
        tree = []

        for c in comments:
            c.children_list = []

        for c in comments:
            if c.parent_comment_id:
                by_id[c.parent_comment_id].children_list.append(c)
            else:
                tree.append(c)

        return tree

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

    def _validate_photo_approved(self):
        if (
            self._photo
            and self._photo.state != "approved"
            and self.cleaned_data["user"] != self._photo.author
        ):
            self.add_error(
                "state",
                ValidationError(
                    message="Просматривать комментарии к неопубликованной фотографии запрещено"
                ),
            )
            self.response_status = status.HTTP_403_FORBIDDEN

from functools import lru_cache

from django import forms
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from service_objects.errors import ValidationError
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Like, User


class LikeDeleteService(ServiceWithResult):
    id = forms.IntegerField(required=True, min_value=1)
    user = ModelField(User)

    custom_validations = ["_validate_photo_exist", "_validate_like_exist"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._delete_like()
        return self

    def _delete_like(self):
        like = self._like
        like.delete()
        return like

    @property
    @lru_cache
    def _photo(self):
        try:
            return Like.objects.filter(photo_id=self.cleaned_data["id"])
        except ObjectDoesNotExist:
            return None

    @property
    @lru_cache
    def _like(self):
        try:
            return Like.objects.get(
                user_id=self.cleaned_data["user"].id, photo_id=self.cleaned_data["id"]
            )
        except ObjectDoesNotExist:
            return None

    def _validate_photo_exist(self):
        if not self._photo:
            self.add_error(
                "photo", ValidationError(message="Запрошенной фотографии нет")
            )
            self.response_status = status.HTTP_404_NOT_FOUND

    def _validate_like_exist(self):
        if self._photo and not self._like:
            self.add_error("id", ValidationError(message="Лайк не найден"))
            self.response_status = status.HTTP_404_NOT_FOUND

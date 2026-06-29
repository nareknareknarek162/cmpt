from django import forms
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from service_objects.errors import ValidationError
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Like, Photo, User


class LikesShowService(ServiceWithResult):
    id = forms.IntegerField(required=True)
    user = ModelField(User, required=False)

    custom_validations = ["_validate_photo_exist"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = {"likes": self._likes(), "liked": self._is_liked()}
        return self

    def _is_liked(self):
        if self.cleaned_data["user"]:
            return Like.objects.filter(
                user_id=self.cleaned_data["user"].id, photo_id=self.cleaned_data["id"]
            ).exists()
        return False

    def _likes(self):
        return Like.objects.filter(photo_id=self.cleaned_data["id"])

    @property
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

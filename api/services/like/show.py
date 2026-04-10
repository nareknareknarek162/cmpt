from django import forms
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from service_objects.errors import ValidationError
from service_objects.services import ServiceWithResult

from models_app.models import Like


class LikesShowService(ServiceWithResult):
    id = forms.IntegerField(required=True)

    custom_validations = ["_validate_photo_exist"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._likes()
        return self

    def _likes(self):
        return self._photo

    @property
    def _photo(self):
        try:
            return Like.objects.filter(photo_id=self.cleaned_data["id"])
        except ObjectDoesNotExist:
            return None

    def _validate_photo_exist(self):
        if not self._photo:
            self.add_error(
                "photo", ValidationError(message="Запрошенной фотографии не существует")
            )
            self.response_status = status.HTTP_404_NOT_FOUND

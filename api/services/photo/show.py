from functools import lru_cache

from django import forms
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from service_objects.services import ServiceWithResult

from models_app.models import Photo


class PhotoShowService(ServiceWithResult):
    id = forms.IntegerField(min_value=1, required=True)

    custom_validations = ["_validate_photo_exists"]

    def process(self):
        self.run_custom_validations()

        if self.is_valid():
            self.result = self._photo
        else:
            self.service_clean()
        return self

    @property
    @lru_cache
    def _photo(self):
        try:
            return Photo.objects.get(id=self.cleaned_data["id"])
        except ObjectDoesNotExist:
            return None

    def _validate_photo_exists(self):
        if not self._photo:
            self.add_error("id", ValidationError(message="Запрошенной фотографии нет"))

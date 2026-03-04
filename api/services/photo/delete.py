from functools import lru_cache

from django import forms
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Photo, User


class PhotoDeleteService(ServiceWithResult):
    id = forms.IntegerField(min_value=1, required=True)
    user = ModelField(User)
    custom_validations = ["_validate_photo_exists", "_validate_author"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._delete_photo()
        else:
            self.service_clean()
        return self

    def _delete_photo(self):
        photo = self._photo
        photo.delete()

        return photo

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

    def _validate_author(self):
        if self._photo and self.cleaned_data["user"].id != self._photo.author_id:
            self.add_error("id", ValidationError(message="Нет доступа"))

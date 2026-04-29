from functools import lru_cache

from django import forms
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework import status
from service_objects.services import ServiceWithResult

from models_app.models import Photo


class PhotoScheduleDeleteService(ServiceWithResult):
    id = forms.IntegerField(min_value=1, required=True)
    user = forms.IntegerField(min_value=1)
    custom_validations = ["_validate_photo_exists", "_validate_author"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._schedule_delete_photo()
        return self

    def _schedule_delete_photo(self):
        photo = self._photo
        photo.state = "on_delete"  # плохо
        photo.save()

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
            self.response_status = status.HTTP_404_NOT_FOUND

    def _validate_author(self):
        if self._photo and self.cleaned_data["user"] != self._photo.author_id:
            self.add_error("id", ValidationError(message="Нет доступа"))
            self.response_status = status.HTTP_403_FORBIDDEN

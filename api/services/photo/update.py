from functools import lru_cache

from django import forms
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from service_objects.errors import ValidationError
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Photo, User
from models_app.models.photo.fsm import State


class PhotoUpdateService(ServiceWithResult):
    id = forms.IntegerField(required=True)
    title = forms.CharField(required=False)
    description = forms.CharField(required=False)
    image = forms.ImageField(required=False)
    user = ModelField(User)

    custom_validations = ["_validate_photo_exist", "_validate_author"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._update_photo()
        return self

    def _update_photo(self):
        photo = self._photo
        for field in ("title", "description", "image"):
            value = self.cleaned_data.get(field)
            if value not in (None, ""):
                setattr(photo, field, self.cleaned_data[field])
        photo.state = State.ON_MODERATION

        photo.save()
        return photo

    @property
    @lru_cache
    def _photo(self):
        try:
            return Photo.objects.get(id=self.cleaned_data["id"])
        except ObjectDoesNotExist:
            return None

    def _validate_photo_exist(self):
        if not self._photo:
            self.add_error("id", ValidationError(message="Запрошенной фотографии нет"))
            self.response_status = status.HTTP_404_NOT_FOUND

    def _validate_author(self):
        if self._photo and self.cleaned_data["user"].id != self._photo.author_id:
            self.add_error("id", ValidationError(message="Нет доступа"))
            self.response_status = status.HTTP_403_FORBIDDEN

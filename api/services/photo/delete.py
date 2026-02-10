from django import forms
from django.core.exceptions import ObjectDoesNotExist
from service_objects.services import ServiceWithResult

from models_app.models import Photo


class PhotoDeleteService(ServiceWithResult):
    id = forms.IntegerField(min_value=1, required=True)

    def process(self):
        self.result = self._delete_photo()
        return self

    def _delete_photo(self):
        try:
            photo = Photo.objects.get(id=self.cleaned_data["id"])
        except ObjectDoesNotExist:
            return None

        photo.delete()
        return photo

from django import forms
from service_objects.services import ServiceWithResult

from models_app.models import Photo


class PhotoShowService(ServiceWithResult):
    id = forms.IntegerField(min_value=1, required=True)

    def process(self):
        self.result = self._photo()
        return self

    def _photo(self):
        return Photo.objects.get(id=self.cleaned_data["id"])

from django import forms
from service_objects.services import ServiceWithResult

from models_app.models import Photo
from models_app.models.photo.fsm import State


class PhotoUpdateService(ServiceWithResult):
    id = forms.IntegerField(required=True)
    author_id = forms.IntegerField(required=True)
    title = forms.CharField(required=False)
    description = forms.CharField(required=False)
    image = forms.ImageField(required=True)

    def process(self):
        self.result = self._update_photo()
        return self

    def _update_photo(self):
        photo = Photo.objects.get(id=self.cleaned_data["id"])
        photo.title = self.cleaned_data["title"]
        photo.description = self.cleaned_data["description"]
        photo.image = self.cleaned_data["image"]
        photo.state = State.ON_MODERATION
        photo.save()

        return photo

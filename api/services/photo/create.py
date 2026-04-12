from django import forms
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import Photo, User


class PhotoCreateService(ServiceWithResult):
    title = forms.CharField(required=True, min_length=1, max_length=127)
    description = forms.CharField(required=True, min_length=1, max_length=511)
    image = forms.ImageField(required=True)
    author = ModelField(User)

    def process(self):
        self.result = self._create_photo()
        return self

    def _create_photo(self):
        photo = Photo.objects.create(
            author_id=self.cleaned_data["author"].id,
            title=self.cleaned_data.get("title"),
            description=self.cleaned_data.get("description"),
            image=self.cleaned_data["image"],
        )

        return photo

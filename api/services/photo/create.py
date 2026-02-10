from django import forms
from service_objects.services import ServiceWithResult

from models_app.models import Photo


class PhotoCreateService(ServiceWithResult):
    author_id = forms.IntegerField(required=True)
    title = forms.CharField(required=False)
    description = forms.CharField(required=False)
    image = forms.ImageField(required=True)

    def process(self):
        self.result = self._create_photo()
        return self

    def _create_photo(self):
        photo = Photo.objects.create(
            author_id=self.cleaned_data["author_id"],
            title=self.cleaned_data.get("title"),
            description=self.cleaned_data.get("description"),
            image=self.cleaned_data["image"],
        )

        return photo

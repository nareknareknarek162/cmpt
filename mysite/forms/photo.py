from django import forms
from django.forms import ModelForm

from models_app.models import Photo


class PhotoForm(ModelForm):
    description = forms.CharField(
        max_length=511,
        required=True,
        widget=forms.Textarea(
            attrs={"rows": 4, "class": "form-control", "id": "photo-description"}
        ),
    )
    title = forms.CharField(
        max_length=127,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "id": "photo-title"}),
    )

    image = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={"class": "form-control", "id": "photo-image"}
        )
    )

    class Meta:
        model = Photo
        fields = ["image", "title", "description"]

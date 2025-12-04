from django import forms
from django.forms import ModelForm

from models_app.models import Photo


class PhotoForm(ModelForm):
    description = forms.CharField(
        max_length=511,
        required=True,
        widget=forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
    )

    class Meta:
        model = Photo
        fields = ["image", "description"]

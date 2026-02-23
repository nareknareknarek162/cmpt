from django import forms
from service_objects.services import ServiceWithResult

from models_app.models import User


class UserUpdateService(ServiceWithResult):
    id = forms.IntegerField(required=True)
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    birth_date = forms.DateField()
    password = forms.CharField()
    gender = forms.ChoiceField(choices=[("M", "Мужской"), ("F", "Женский")])

    def process(self):
        self.result = self._update_photo()
        return self

    def _update_photo(self):
        user = User.objects.get(id=self.cleaned_data["id"])
        user.username = self.cleaned_data["username"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.birth_date = self.cleaned_data["birth_date"]
        user.password = self.cleaned_data["password"]
        user.gender = self.cleaned_data["gender"]
        user.save()

        return user

from django import forms
from service_objects.services import ServiceWithResult

from models_app.models import User


class UserShowService(ServiceWithResult):
    id = forms.IntegerField(min_value=1, required=True)

    def process(self):
        self.result = self._user()
        return self

    def _user(self):
        return User.objects.get(id=self.cleaned_data["id"])

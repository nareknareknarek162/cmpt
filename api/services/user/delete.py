from django import forms
from django.core.exceptions import ObjectDoesNotExist
from service_objects.services import ServiceWithResult

from models_app.models import User


class UserDeleteService(ServiceWithResult):
    id = forms.IntegerField(min_value=1, required=True)

    def process(self):
        self.result = self._delete_user()
        return self

    def _delete_user(self):
        try:
            user = User.objects.get(id=self.cleaned_data["id"])
        except ObjectDoesNotExist:
            return None

        user.delete()
        return user

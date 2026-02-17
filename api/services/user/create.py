from django import forms
from service_objects.services import ServiceWithResult

from models_app.models import User


class UserCreateService(ServiceWithResult):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    birth_date = forms.DateTimeField(required=True)
    password = forms.CharField(required=True)
    gender = forms.ChoiceField(
        required=True, choices=[("M", "Мужской"), ("F", "Женский")]
    )

    def process(self):
        self.result = self._create_user()
        return self

    def _create_user(self):
        user = User(
            username=self.cleaned_data["username"],
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
            email=self.cleaned_data["email"],
            birth_date=self.cleaned_data["birth_date"],
            is_staff=False,
            is_active=True,
            gender=self.cleaned_data["gender"],
        )
        user.set_password(self.cleaned_data["password"])
        user.save()

        return user

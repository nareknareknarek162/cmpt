from django import forms
from django.utils import timezone
from rest_framework import status
from service_objects.errors import ValidationError
from service_objects.services import ServiceWithResult

from models_app.models import User


class UserCreateService(ServiceWithResult):
    username = forms.CharField(required=True, min_length=2, max_length=20)
    first_name = forms.CharField(required=True, min_length=1, max_length=30)
    last_name = forms.CharField(required=True, min_length=1, max_length=30)
    email = forms.EmailField(required=True)
    birth_date = forms.DateField(required=True)
    password = forms.CharField(required=True)
    gender = forms.ChoiceField(
        required=True, choices=[("M", "Мужской"), ("F", "Женский")]
    )

    custom_validations = ["_validate_birth_date"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
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

    def _validate_birth_date(self):
        if self.cleaned_data["birth_date"] > timezone.now().date():
            self.add_error(
                "birth_date",
                ValidationError(message="Дата рождения не может быть в будущем"),
            )
            self.response_status = status.HTTP_400_BAD_REQUEST

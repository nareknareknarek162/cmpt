from django import forms
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import User


class UserUpdateService(ServiceWithResult):
    username = forms.CharField(required=False, min_length=2, max_length=20)
    first_name = forms.CharField(required=False, min_length=1, max_length=30)
    last_name = forms.CharField(required=False, min_length=1, max_length=30)
    email = forms.EmailField(
        required=False,
    )
    birth_date = forms.DateField(required=False)
    password = forms.CharField(
        required=False,
    )
    gender = forms.ChoiceField(
        required=False, choices=[("M", "Мужской"), ("F", "Женский")]
    )
    avatar = forms.ImageField(required=False)
    user = ModelField(User)

    def process(self):
        self.result = self._update_user()
        return self

    def _update_user(self):
        user = User.objects.get(id=self.cleaned_data["user"].id)
        for field in (
            "username",
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "password",
            "gender",
            "avatar",
        ):
            value = self.cleaned_data.get(field)
            if value not in (None, ""):
                setattr(user, field, self.cleaned_data[field])
        user.save()

        return user

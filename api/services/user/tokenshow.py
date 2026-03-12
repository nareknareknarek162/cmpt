from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

from models_app.models import User


class UserTokenShowService(ServiceWithResult):
    user = ModelField(User)

    def process(self):
        self.result = self._user()
        return self

    def _user(self):
        return self.cleaned_data["user"]

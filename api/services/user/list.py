from service_objects.services import ServiceWithResult

from models_app.models import User


class UserListShowService(ServiceWithResult):

    def process(self):
        self.result = self._user_list()
        return self

    def _user_list(self):
        return User.objects.all()

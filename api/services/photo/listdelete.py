from service_objects.services import ServiceWithResult

from models_app.models import Photo


class PhotoListDeleteService(ServiceWithResult):

    def process(self):
        self.result = self._delete_photos()
        return self

    def _delete_photos(self):
        return Photo.objects.all().delete()

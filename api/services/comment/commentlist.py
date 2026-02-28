from service_objects.services import ServiceWithResult

from models_app.models import Comment


class CommentShowListService(ServiceWithResult):
    def process(self):
        self.result = self._photo()
        return self

    def _photo(self):
        return Comment.objects.all()

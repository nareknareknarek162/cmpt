from django import forms
from service_objects.services import ServiceWithResult

from models_app.models import Comment


class CommentShowListService(ServiceWithResult):
    id = forms.IntegerField(min_value=1, required=True)

    def process(self):
        self.result = self._build_tree()
        return self

    def _comments(self):
        return Comment.objects.filter(photo=self.cleaned_data["id"])

    def _build_tree(self):
        comments = self._comments()
        by_id = {c.id: c for c in comments}
        tree = []

        for c in comments:
            c.children_list = []

        for c in comments:
            if c.parent_comment_id:
                by_id[c.parent_comment_id].children_list.append(c)
            else:
                tree.append(c)

        return tree

from django.db.models import Count
from django.views.generic import ListView

from models_app.models import Photo


class IndexView(ListView):
    model = Photo
    paginate_by = 6
    template_name = "index.html"
    context_object_name = "photos"

    def get_queryset(self):
        sorting_feature = self.request.GET.get("sort")
        query = super().get_queryset()
        if sorting_feature == "likes":
            query.annotate(likes_count=Count("like")).order_by("-likes_count")
            return query
        if sorting_feature == "comments":
            query.annotate(comments_count=Count("comment")).order_by("-comments_count")
        return query.order_by("publication_date")

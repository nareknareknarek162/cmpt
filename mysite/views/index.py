from django.db.models import Count
from django.views.generic import ListView

from models_app.models import Photo


class IndexView(ListView):
    model = Photo
    paginate_by = 6
    template_name = "index.html"
    context_object_name = "photos"

    def get_queryset(self):
        query = super().get_queryset()
        # сортировка
        if "sort" in self.request.GET:
            sorting_feature = self.request.GET.get("sort")

            if sorting_feature == "likes":
                return query.annotate(likes_count=Count("like")).order_by(
                    "-likes_count"
                )
            if sorting_feature == "comments":
                return query.annotate(comments_count=Count("comment")).order_by(
                    "-comments_count"
                )
            if sorting_feature == "publication_date":
                return query.order_by("publication_date")

        # фильтр
        if "filter" in self.request.GET:
            filter_feature = self.request.GET.get("filter")
            filter_query_value = self.request.GET.get("filter_query")

            if filter_feature == "username":
                return query.filter(author__username__icontains=filter_query_value)
            if filter_feature == "description":
                return query.filter(description__icontains=filter_query_value)
            if filter_feature == "title":
                pass

        return query.order_by("publication_date")

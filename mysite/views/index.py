from django.db.models import Count, Q
from django.views.generic import ListView

from models_app.models import Photo


class IndexView(ListView):
    model = Photo
    paginate_by = 6
    template_name = "index.html"
    context_object_name = "photos"

    def get_queryset(self):
        query = super().get_queryset()
        search = self.request.GET.get("search")

        # фильтр
        if search:
            query = query.filter(
                Q(description__icontains=search) | Q(author__username__icontains=search)
            )

        # сортировка
        if "sort" in self.request.GET:
            sorting_feature = self.request.GET.get("sort")

            if sorting_feature == "likes":
                query = query.annotate(likes_count=Count("like")).order_by(
                    "-likes_count"
                )
            elif sorting_feature == "comments":
                query = query.annotate(comments_count=Count("comment")).order_by(
                    "-comments_count"
                )
            elif sorting_feature == "publication_date":
                query = query.order_by("publication_date")

        return query

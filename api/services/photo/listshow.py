from django import forms
from django.db.models import Count, Q
from service_objects.services import ServiceWithResult

from models_app.models import Photo


class PhotoListShowService(ServiceWithResult):
    search = forms.CharField(required=False)
    sort = forms.CharField(required=False)
    order = forms.CharField(required=False)

    def process(self):
        query = self._photos()
        query = self._search(query)
        query = self._sort(query)
        self.result = query
        return self

    def _photos(self):
        return Photo.objects.all()

    def _search(self, queryset):
        search = self.cleaned_data.get("search")
        if search:
            queryset = queryset.filter(
                Q(description__icontains=search)
                | Q(author__username__icontains=search)
                | Q(title__icontains=search)
            )
        return queryset

    def _sort(self, queryset):
        sorting_feature = self.cleaned_data.get("sort")
        order = self.cleaned_data.get("order")

        if sorting_feature:
            if sorting_feature == "likes":
                queryset = queryset.annotate(likes_count=Count("like")).order_by(
                    f"{order}likes_count"
                )
            elif sorting_feature == "comments":
                queryset = queryset.annotate(comments_count=Count("comment")).order_by(
                    f"{order}comments_count"
                )
            elif sorting_feature == "publication_date":
                queryset = queryset.order_by("publication_date")

        return queryset

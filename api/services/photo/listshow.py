from django import forms
from django.core.paginator import EmptyPage, Paginator
from django.db.models import Count, Q
from rest_framework import status
from service_objects.errors import AuthenticationFailed
from service_objects.fields import ModelField
from service_objects.services import ServiceWithResult

import config.settings.restframework as settings
from models_app.models import Photo, User


class PhotoListShowService(ServiceWithResult):
    search = forms.CharField(required=False)
    sort = forms.CharField(required=False)
    order = forms.CharField(required=False)
    mine = forms.BooleanField(required=False)
    user = ModelField(User, required=False)
    page = forms.IntegerField(required=False, min_value=1, initial=1)
    per_page = forms.IntegerField(required=False, min_value=1, max_value=100, initial=6)

    custom_validations = ["_validate_user_presence"]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._photos()
        return self

    def _photos(self):
        try:
            return Paginator(
                self._sorted_photo(),
                per_page=self.cleaned_data.get("per_page")
                or settings.REST_FRAMEWORK["PAGE_SIZE"],
            ).page(self.cleaned_data.get("page") or 1)
        except EmptyPage:
            return Paginator(
                Photo.objects.none(),
                per_page=self.cleaned_data.get("per_page")
                or settings.REST_FRAMEWORK["PAGE_SIZE"],
            ).page(1)

    def _filtered_photos(self):
        queryset = Photo.objects.all()
        search = self.cleaned_data.get("search")
        mine = self.cleaned_data.get("mine")
        if search:
            queryset = queryset.filter(
                Q(description__icontains=search)
                | Q(author__username__icontains=search)
                | Q(title__icontains=search)
            )
        if mine:
            queryset = queryset.filter(author=self.cleaned_data["user"])
        return queryset

    def _sorted_photo(self):
        queryset = self._filtered_photos()
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

    def _validate_user_presence(self):
        if self.cleaned_data.get("mine") and not self.cleaned_data.get("user"):
            self.add_error(
                "mine",
                AuthenticationFailed(
                    message="Для просмотра своих фотографий требуется авторизация"
                ),
            )
            self.response_status = status.HTTP_401_UNAUTHORIZED

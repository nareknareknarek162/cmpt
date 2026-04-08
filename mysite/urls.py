from django.urls import path

from mysite.views import (
    AccountView,
    AddPhotoView,
    AuthView,
    DetailedPhotoView,
    EditPhotoView,
    IndexView,
    RegistrationView,
    Yandex,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("photo/<int:pk>/", DetailedPhotoView.as_view(), name="details"),
    path("auth/", AuthView.as_view(), name="auth"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("account/", AccountView.as_view(), name="account"),
    path("photos/add/", AddPhotoView.as_view(), name="add-photo"),
    path("photos/edit/<int:pk>/", EditPhotoView.as_view(), name="edit-photo"),
    path("oauth/yandex/", Yandex.as_view(), name="callback"),
]

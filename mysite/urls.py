from django.urls import path

from mysite.views import (
    AccountView,
    AddPhotoView,
    AuthView,
    DetailedPhotoView,
    IndexView,
    Logout,
    RegistrationView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("photos/<int:pk>", DetailedPhotoView.as_view(), name="details"),
    path("auth/", AuthView.as_view(), name="auth"),
    path("logout/", Logout.as_view(), name="logout"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("account/", AccountView.as_view(), name="account"),
    path("photos/add", AddPhotoView.as_view(), name="add-photo"),
]

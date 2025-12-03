from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("photos/<int:pk>", views.DetailedPhotoView.as_view(), name="details"),
    path("auth/", views.AuthView.as_view(), name="auth"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("registration/", views.RegistrationView.as_view(), name="registration"),
    path("account/", views.AccountView.as_view(), name="account"),
    path("photos/add", views.AddPhotoView.as_view(), name="add-photo"),
]

from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("auth/", views.AuthView.as_view(), name="auth"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("registration/", views.RegistrationView.as_view(), name="registration"),
]

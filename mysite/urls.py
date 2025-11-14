from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("auth/", views.authorisation_page, name="auth"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("registration/", views.registration_view, name="registration"),
    path("registrate/", views.registrate_view, name='registrate')
]

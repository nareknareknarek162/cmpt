from django.urls import path

from api.views.photo import RetrievePhotoView

urlpatterns = [path("photo/<int:id>/", RetrievePhotoView.as_view())]

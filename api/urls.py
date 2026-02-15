from django.urls import path

from api.views.comment import RetrieveCommentView
from api.views.photo import PhotoListCreateView, RetrievePhotoView
from api.views.user import RetrieveUserView

urlpatterns = [
    path("photo/", PhotoListCreateView.as_view()),
    path("photo/<int:id>/", RetrievePhotoView.as_view()),
    path("user/<int:id>/", RetrieveUserView.as_view()),
    path("comment/<int:id>/", RetrieveCommentView.as_view()),
]

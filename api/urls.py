from django.urls import path

from api.views.comment import RetrieveCommentView
from api.views.likes import RetrieveListLikesView
from api.views.photo import PhotoListCreateView, RetrievePhotoView
from api.views.user import RetrieveUserView, UserListCreateView

urlpatterns = [
    path("photo/", PhotoListCreateView.as_view()),
    path("photo/<int:id>/", RetrievePhotoView.as_view()),
    path("user/<int:id>/", RetrieveUserView.as_view()),
    path("user/", UserListCreateView.as_view()),
    path("likes/photo/<int:id>/", RetrieveListLikesView.as_view()),
    path("comment/<int:id>/", RetrieveCommentView.as_view()),
]

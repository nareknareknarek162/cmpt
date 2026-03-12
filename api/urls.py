from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.views.comment import CommentListCreateView, RetrieveCommentView
from api.views.likes import CreateLikesView, RetrieveListLikesView
from api.views.photo import PhotoDetailView, PhotoListCreateView
from api.views.user import RetrieveUserTokenView, RetrieveUserView, UserListCreateView

urlpatterns = [
    path("photo/", PhotoListCreateView.as_view()),
    path("photo/<int:id>/", PhotoDetailView.as_view()),
    path("user/<int:id>/", RetrieveUserView.as_view()),
    path("user/", UserListCreateView.as_view()),
    path("user/me/", RetrieveUserTokenView.as_view()),
    path("like/photo/<int:id>/", CreateLikesView.as_view()),
    path("like/photo/<int:id>/list/", RetrieveListLikesView.as_view()),
    path("comment/<int:id>/", RetrieveCommentView.as_view()),
    path("comment/photos/", CommentListCreateView.as_view()),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

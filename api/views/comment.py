from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.docs.comment import (
    CREATE_COMMENT,
    DELETE_COMMENT,
    PATCH_COMMENT,
    SHOW_COMMENT,
    SHOW_COMMENTS_LIST,
)
from api.serializers.comment.show import CommentShowSerializer
from api.services.comment.create import CommentCreateService
from api.services.comment.delete import CommentDeleteService
from api.services.comment.show import CommentShowService
from api.services.comment.showlist import CommentShowListService
from api.services.comment.update import CommentUpdateService


class RetrieveCommentView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @extend_schema(**SHOW_COMMENT)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(CommentShowService, {"id": kwargs["id"]})
        return Response(
            CommentShowSerializer(outcome.result).data, status=status.HTTP_200_OK
        )

    @extend_schema(**PATCH_COMMENT)
    def patch(self, request, *args, **kwargs):
        outcome = ServiceOutcome(CommentUpdateService, {"id": kwargs["id"]})
        return Response(
            CommentShowSerializer(outcome.result).data, status=status.HTTP_200_OK
        )

    @extend_schema(**DELETE_COMMENT)
    def delete(self, request, *args, **kwargs):
        ServiceOutcome(CommentDeleteService, {"id": kwargs["id"], "user": request.user})
        return Response(None, status=status.HTTP_200_OK)


class CommentListView(APIView):
    @extend_schema(**SHOW_COMMENTS_LIST)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(CommentShowListService, {"id": kwargs["id"]})
        return Response(
            CommentShowSerializer(outcome.result, many=True).data,
            status=status.HTTP_200_OK,
        )


class CommentCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @extend_schema(**CREATE_COMMENT)
    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(
            CommentCreateService,
            {"id": kwargs["id"], "author": request.user} | request.data,
        )
        return Response(
            CommentShowSerializer(outcome.result).data, status=status.HTTP_201_CREATED
        )

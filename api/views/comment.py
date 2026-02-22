from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.docs.comment import SHOW_COMMENT
from api.serializers.comment.show import CommentShowSerializer
from api.services.comment.delete import CommentDeleteService
from api.services.comment.show import CommentShowService


class RetrieveCommentView(APIView):

    @extend_schema(**SHOW_COMMENT)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(CommentShowService, {"id": kwargs["id"]})
        return Response(
            CommentShowSerializer(outcome.result).data, status=status.HTTP_200_OK
        )

    def delete(self, request, *args, **kwargs):
        outcome = ServiceOutcome(CommentDeleteService, {"id": kwargs["id"]})
        return Response(None, status=status.HTTP_200_OK)

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.docs.like import CREATE_LIKE, SHOW_LIKES
from api.serializers.likes.show import LikeShowSerializer
from api.services.like.create import LikeCreateService
from api.services.like.delete import LikeDeleteService
from api.services.like.show import LikesShowService


class RetrieveListLikesView(APIView):

    @extend_schema(**SHOW_LIKES)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(LikesShowService, {"id": kwargs["id"]})
        return Response(
            LikeShowSerializer(outcome.result, many=True).data,
            status=status.HTTP_200_OK,
        )


class CreateListLikesView(APIView):

    permission_classes = [IsAuthenticated]

    @extend_schema(**CREATE_LIKE)
    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(
            LikeCreateService,
            {"photo_id": kwargs["photo_id"], "user": request.data.user},
        )
        return Response(
            LikeShowSerializer(outcome.result).data,
            status=status.HTTP_201_CREATED,
        )

    def delete(self, request, *args, **kwargs):
        outcome = ServiceOutcome(
            LikeDeleteService,
            {"photo_id": kwargs["photo_id"]},
        )
        return Response(None, status=status.HTTP_200_OK)

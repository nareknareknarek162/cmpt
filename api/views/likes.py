from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.docs.like import CREATE_LIKE, DELETE_LIKE, SHOW_LIKES
from api.serializers.likes.create import LikeCreateSerializer
from api.serializers.likes.show import LikesResponseSerializer
from api.services.like.create import LikeCreateService
from api.services.like.delete import LikeDeleteService
from api.services.like.showlist import LikesShowService


class RetrieveListLikesView(APIView):

    @extend_schema(**SHOW_LIKES)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(
            LikesShowService,
            {
                "id": kwargs["id"],
                "user": request.user if request.user.is_authenticated else None,
            },
        )
        return Response(
            LikesResponseSerializer(outcome.result).data,
            status=status.HTTP_200_OK,
        )


class CreateLikesView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    @extend_schema(**CREATE_LIKE)
    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(
            LikeCreateService,
            {"id": kwargs["id"], "user": request.user},
        )
        return Response(
            LikeCreateSerializer(outcome.result).data,
            status=status.HTTP_201_CREATED,
        )

    @extend_schema(**DELETE_LIKE)
    def delete(self, request, *args, **kwargs):
        ServiceOutcome(
            LikeDeleteService,
            {"id": kwargs["id"], "user": request.user},
        )
        return Response(None, status=status.HTTP_200_OK)

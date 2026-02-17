from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.docs.like import SHOW_LIKES
from api.serializers.likes.show import LikeShowSerializer
from api.services.like.show import LikesShowService


class RetrieveListLikesView(APIView):

    @extend_schema(**SHOW_LIKES)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(LikesShowService, {"id": kwargs["id"]})
        return Response(
            LikeShowSerializer(outcome.result, many=True).data,
            status=status.HTTP_200_OK,
        )

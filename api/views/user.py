from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.docs.user import DELETE_USER, SHOW_USER
from api.serializers.user.delete import UserDeleteSerializer
from api.serializers.user.show import UserShowSerializer
from api.services.user.delete import UserDeleteService
from api.services.user.show import UserShowService


class RetrieveUserView(APIView):

    @extend_schema(**SHOW_USER)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(UserShowService, {"id": kwargs["id"]})
        return Response(
            UserShowSerializer(outcome.result).data, status=status.HTTP_200_OK
        )

    @extend_schema(**DELETE_USER)
    def delete(self, request, *args, **kwargs):

        outcome = ServiceOutcome(UserDeleteService, {"id": kwargs["id"]})
        return Response(
            UserDeleteSerializer(outcome.result).data, status=status.HTTP_200_OK
        )


from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.docs.user import (
    CREATE_USER,
    DELETE_USER,
    SHOW_USER,
    SHOW_USER_BY_TOKEN,
    SHOW_USER_LIST,
    UPDATE_USER,
)
from api.serializers.user.create import UserCreateSerializer
from api.serializers.user.show import UserShowSerializer
from api.services.user.create import UserCreateService
from api.services.user.current import UserCurrentService
from api.services.user.delete import UserDeleteService
from api.services.user.show import UserShowService
from api.services.user.showlist import UserListShowService
from api.services.user.update import UserUpdateService


class RetrieveUserView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @extend_schema(**SHOW_USER)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(UserShowService, {"id": kwargs["id"]})
        return Response(
            UserShowSerializer(outcome.result).data, status=status.HTTP_200_OK
        )

    @extend_schema(**DELETE_USER)
    def delete(self, request, *args, **kwargs):
        ServiceOutcome(UserDeleteService, {"id": kwargs["id"]})
        return Response(None, status=status.HTTP_200_OK)


class UserListCreateView(APIView):

    @extend_schema(**SHOW_USER_LIST)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(UserListShowService, {})
        return Response(
            UserShowSerializer(outcome.result, many=True).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(**CREATE_USER)
    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(UserCreateService, request.data)
        return Response(
            UserCreateSerializer(outcome.result).data, status=status.HTTP_201_CREATED
        )


class RetrieveUserTokenView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(**SHOW_USER_BY_TOKEN)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(UserCurrentService, {"user": request.user})
        return Response(
            UserShowSerializer(outcome.result).data, status=status.HTTP_200_OK
        )

    @parser_classes([MultiPartParser])
    @extend_schema(**UPDATE_USER)
    def patch(self, request, *args, **kwargs):
        outcome = ServiceOutcome(
            UserUpdateService,
            {"user": request.user if request.user.is_authenticated else None}
            | request.data.dict(),
            request.FILES,
        )
        return Response(
            UserShowSerializer(outcome.result).data, status=status.HTTP_200_OK
        )

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.docs.photo import (
    CREATE_PHOTO,
    DELETE_LIST_PHOTO,
    DELETE_PHOTO,
    PATCH_PHOTO,
    SHOW_LIST_PHOTO,
    SHOW_PHOTO,
)
from api.serializers.photo.show import PhotoShowSerializer
from api.serializers.photo.showdeatil import PhotoShowDetailSerializer
from api.services.photo.create import PhotoCreateService
from api.services.photo.delete import PhotoDeleteService
from api.services.photo.listdelete import PhotoListDeleteService
from api.services.photo.listshow import PhotoListShowService
from api.services.photo.show import PhotoShowService
from api.services.photo.update import PhotoUpdateService


class RetrievePhotoView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticatedOrReadOnly]

    @extend_schema(**SHOW_PHOTO)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(PhotoShowService, {"id": kwargs["id"]})
        return Response(
            PhotoShowDetailSerializer(outcome.result).data, status=status.HTTP_200_OK
        )

    @extend_schema(**DELETE_PHOTO)
    def delete(self, request, *args, **kwargs):
        outcome = ServiceOutcome(PhotoDeleteService, {"id": kwargs["id"]})
        return Response(None, status=status.HTTP_200_OK)

    @extend_schema(**PATCH_PHOTO)
    def patch(self, request, *args, **kwargs):
        outcome = ServiceOutcome(
            PhotoUpdateService,
            {"id": kwargs["id"], "user": request.user} | request.data.dict(),
            request.FILES,
        )
        return Response(
            PhotoShowDetailSerializer(outcome.result).data, status=status.HTTP_200_OK
        )


class PhotoListCreateView(APIView):
    parser_classes = [MultiPartParser]

    @extend_schema(**CREATE_PHOTO)
    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(PhotoCreateService, request.data, request.FILES)
        return Response(
            PhotoShowSerializer(outcome.result).data, status=status.HTTP_201_CREATED
        )

    @extend_schema(**SHOW_LIST_PHOTO)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(PhotoListShowService, {})
        return Response(
            PhotoShowSerializer(outcome.result, many=True).data,
            status=status.HTTP_200_OK,
        )

    @extend_schema(**DELETE_LIST_PHOTO)
    def delete(self, request, *args, **kwargs):
        outcome = ServiceOutcome(PhotoListDeleteService, {})
        return Response(None, status=status.HTTP_200_OK)

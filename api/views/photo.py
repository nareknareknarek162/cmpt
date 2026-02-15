from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.docs.photo import CREATE_PHOTO, DELETE_PHOTO, SHOW_PHOTO
from api.serializers.photo.show import PhotoShowSerializer
from api.services.photo.create import PhotoCreateService
from api.services.photo.delete import PhotoDeleteService
from api.services.photo.show import PhotoShowService


class RetrievePhotoView(APIView):

    @extend_schema(**SHOW_PHOTO)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(PhotoShowService, {"id": kwargs["id"]})
        return Response(
            PhotoShowSerializer(outcome.result).data, status=status.HTTP_200_OK
        )

    @extend_schema(**DELETE_PHOTO)
    def delete(self, request, *args, **kwargs):
        outcome = ServiceOutcome(PhotoDeleteService, {"id": kwargs["id"]})
        return Response(None, status=status.HTTP_200_OK)


class PhotoListCreateView(APIView):
    parser_classes = [MultiPartParser]

    @extend_schema(**CREATE_PHOTO)
    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(PhotoCreateService, request.data, request.FILES)
        return Response(
            PhotoShowSerializer(outcome.result).data, status=status.HTTP_201_CREATED
        )

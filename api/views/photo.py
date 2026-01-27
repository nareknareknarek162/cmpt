from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from service_objects.services import ServiceOutcome

from api.docs.photo import SHOW_PHOTO
from api.serializers.photo import PhotoShowSerializer
from api.services.photo.show import PhotoShowService


class RetrievePhotoView(APIView):

    @extend_schema(**SHOW_PHOTO)
    def get(self, request, *args, **kwargs):
        outcome = ServiceOutcome(PhotoShowService, {"id": kwargs["id"]})
        return Response(
            PhotoShowSerializer(outcome.result).data, status=status.HTTP_200_OK
        )

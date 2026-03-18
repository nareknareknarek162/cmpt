from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter

from api.serializers.photo.delete import PhotoDeleteSerializer
from api.serializers.photo.modify import PhotoModifySerializer
from api.serializers.photo.show import PhotoShowSerializer
from utils.docs_typed_dict import DocsDict

SHOW_PHOTO: DocsDict = {
    "tags": ["photo"],
    "description": "Show Photo by Id",
    "responses": {200: PhotoShowSerializer},
}

SHOW_LIST_PHOTO: DocsDict = {
    "tags": ["photo"],
    "description": "Show List of all Photos",
    "responses": {200: PhotoShowSerializer},
    "parameters": [
        OpenApiParameter(
            name="sort",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            required=False,
            description="Sort by date/likes/comments",
            enum=["date", "likes", "comments"],
        ),
        OpenApiParameter(
            name="order",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            required=False,
            description="Order of sorting",
            enum=["-"],
        ),
        OpenApiParameter(
            name="search",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            required=False,
            description="Search string in username/title/description",
        ),
        OpenApiParameter(
            name="mine",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            required=False,
            description="Show photos only owned by currently authorised user",
            enum=["true"],
        ),
    ],
}
DELETE_PHOTO: DocsDict = {
    "tags": ["photo"],
    "description": "Delete Photo by Id",
    "responses": {200: PhotoDeleteSerializer},
}

CREATE_PHOTO: DocsDict = {
    "tags": ["photo"],
    "description": "Create a Photo",
    "request": PhotoModifySerializer,
    "responses": {201: PhotoShowSerializer},
}

PATCH_PHOTO: DocsDict = {
    "tags": ["photo"],
    "description": "Update a Photo",
    "request": PhotoModifySerializer,
    "responses": {200: PhotoShowSerializer},
}

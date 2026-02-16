from api.serializers.photo.create import PhotoCreateSerializer
from api.serializers.photo.delete import PhotoDeleteSerializer
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
}

DELETE_PHOTO: DocsDict = {
    "tags": ["photo"],
    "description": "Delete Photo by Id",
    "responses": {200: PhotoDeleteSerializer},
}

CREATE_PHOTO: DocsDict = {
    "tags": ["photo"],
    "description": "Create a Photo",
    "request": PhotoCreateSerializer,
    "responses": {201: PhotoCreateSerializer},
}

PATCH_PHOTO: DocsDict = {
    "tags": ["photo"],
    "description": "Update a Photo",
    "request": PhotoShowSerializer,
    "responses": {201: PhotoShowSerializer},
}

DELETE_LIST_PHOTO: DocsDict = {
    "tags": ["photo"],
    "description": "Delete Photo by Id",
    "responses": {200: PhotoDeleteSerializer},
}

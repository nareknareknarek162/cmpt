from api.serializers.likes.create import LikeCreateSerializer
from api.serializers.likes.show import LikeShowSerializer
from utils.docs_typed_dict import DocsDict

SHOW_LIKES: DocsDict = {
    "tags": ["likes"],
    "description": "Show Likes by Photo Id",
    "responses": {200: LikeShowSerializer},
}

CREATE_LIKE: DocsDict = {
    "tags": ["like"],
    "description": "Create Like by Photo Id",
    "request": LikeCreateSerializer,
    "responses": {201: LikeCreateSerializer},
}

DELETE_LIKE: DocsDict = {
    "tags": ["like"],
    "description": "Delete Like by Id",
    "responses": {200: LikeShowSerializer},
}

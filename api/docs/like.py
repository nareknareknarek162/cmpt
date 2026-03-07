from api.serializers.likes.create import LikeCreateSerializer
from api.serializers.likes.show import LikeShowSerializer
from utils.docs_typed_dict import DocsDict

SHOW_LIKES: DocsDict = {
    "tags": ["like"],
    "description": "Show amount of Likes by Photo Id",
    "responses": {200: LikeShowSerializer},
}

CREATE_LIKE: DocsDict = {
    "tags": ["like"],
    "description": "Create Like on the Photo by Id",
    "request": LikeCreateSerializer,
    "responses": {201: LikeShowSerializer},
}

DELETE_LIKE: DocsDict = {
    "tags": ["like"],
    "description": "Delete Like on the photo by Id",
    "responses": {200: LikeShowSerializer},
}

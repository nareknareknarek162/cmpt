from api.serializers.likes.show import LikeShowSerializer
from utils.docs_typed_dict import DocsDict

SHOW_LIKES: DocsDict = {
    "tags": ["like"],
    "description": "Show Likes by Photo Id",
    "responses": {200: LikeShowSerializer},
}

CREATE_LIKE: DocsDict = {
    "tags": ["like"],
    "description": "Create Like by Photo Id",
    "request": LikeShowSerializer,
    "responses": {201: LikeShowSerializer},
}

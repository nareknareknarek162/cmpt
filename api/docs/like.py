from api.serializers.likes.create import LikeCreateSerializer
from api.serializers.likes.show import LikeShowSerializer
from utils.docs_typed_dict import DocsDict

SHOW_LIKES: DocsDict = {
    "tags": ["like"],
    "description": "Show List of Likes by Photo Id",
    "responses": {200: LikeShowSerializer},
}

CREATE_LIKE: DocsDict = {
    "tags": ["like"],
    "description": "Create Like on Photo by its Id",
    "responses": {201: LikeShowSerializer},
}

DELETE_LIKE: DocsDict = {
    "tags": ["like"],
    "description": "Delete Like on Photo by its Id",
    "responses": {200: LikeShowSerializer},
}

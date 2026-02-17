from api.serializers.likes.show import LikeShowSerializer
from utils.docs_typed_dict import DocsDict

SHOW_LIKES: DocsDict = {
    "tags": ["like"],
    "description": "Show Likes by Photo Id",
    "responses": {200: LikeShowSerializer},
}

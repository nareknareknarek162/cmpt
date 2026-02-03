from api.serializers.comment import CommentShowSerializer
from utils.docs_typed_dict import DocsDict

SHOW_COMMENT: DocsDict = {
    "tags": ["comment"],
    "description": "Show Comment by Id",
    "responses": {200: CommentShowSerializer},
}

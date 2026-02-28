from api.serializers.comment.create import CommentCreateSerializer
from api.serializers.comment.show import CommentShowSerializer
from utils.docs_typed_dict import DocsDict

SHOW_COMMENT: DocsDict = {
    "tags": ["comment"],
    "description": "Show Comment by Id",
    "responses": {200: CommentShowSerializer},
}

CREATE_COMMENT: DocsDict = {
    "tags": ["comment"],
    "description": "Create Comment by Photo Id",
    "request": CommentCreateSerializer,
    "responses": {200: CommentShowSerializer},
}

DELETE_COMMENT: DocsDict = {
    "tags": ["comment"],
    "description": "Delete Comment by Id",
    "responses": {200: CommentShowSerializer},
}
SHOW_COMMENTS_LIST: DocsDict = {
    "tags": ["comment"],
    "description": "Show all Comments",
    "responses": {200: CommentShowSerializer},
}

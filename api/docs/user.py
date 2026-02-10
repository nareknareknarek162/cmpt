from api.serializers.user.delete import UserDeleteSerializer
from api.serializers.user.show import UserShowSerializer
from utils.docs_typed_dict import DocsDict

SHOW_USER: DocsDict = {
    "tags": ["user"],
    "description": "Show User by Id",
    "responses": {200: UserShowSerializer},
}

DELETE_USER: DocsDict = {
    "tags": ["user"],
    "description": "Delete User by Id",
    "responses": {200: UserDeleteSerializer},
}

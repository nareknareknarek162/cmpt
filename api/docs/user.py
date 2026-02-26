from api.serializers.user.create import UserCreateSerializer
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

CREATE_USER: DocsDict = {
    "tags": ["user"],
    "description": "Create User",
    "request": UserCreateSerializer,
    "responses": {201: UserShowSerializer},
}

UPDATE_USER: DocsDict = {
    "tags": ["user"],
    "description": "Update User by Id",
    "request": UserCreateSerializer,
    "responses": {200: UserShowSerializer},
}

SHOW_USER_LIST: DocsDict = {
    "tags": ["user"],
    "description": "Show list of all Users",
    "responses": {200: UserShowSerializer},
}
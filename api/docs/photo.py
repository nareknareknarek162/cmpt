from api.serializers.photo import PhotoShowSerializer
from utils.docs_typed_dict import DocsDict

SHOW_PHOTO: DocsDict = {
    "tags": ["photo"],
    "description": "Show Photo by Id",
    "responses": {200: PhotoShowSerializer},
}

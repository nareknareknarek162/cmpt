from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def notify_photo_state(photo):
    channel_layer = get_channel_layer()

    message = {
        "type": "photo_state",
        "text": f"Ваша фотография была {photo.state}"
    }

    async_to_sync(channel_layer.group_send)(
        f"user_{photo.author.id}",
        message
    )
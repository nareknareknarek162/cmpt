from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def notify_photo_state_changed(photo):
    channel_layer = get_channel_layer()

    message = {"type": "nform", "text": f"Ваша фотография была {photo.state}"}

    async_to_sync(channel_layer.group_send)(f"user_{photo.author.id}", message)


def notify_photo_liked(photo, username, action):
    channel_layer = get_channel_layer()

    actions = {
        "liked": "оценил",
        "unliked": "убрал оценку с",
    }

    message = {
        "type": "inform",
        "text": f"{username} {actions[action]} фотографию {photo.title}. "
        f"Текущее количество голосов: {photo.likes.count()}",
    }

    async_to_sync(channel_layer.group_send)(f"user_{photo.author.id}", message)


def notify_photo_commented(photo, username):
    channel_layer = get_channel_layer()

    message = {
        "type": "inform",
        "text": f"{username} прокомментировал(а) фотографию {photo.title}. "
        f"Текущее количество комментариев: {photo.comments.count()}",
    }

    async_to_sync(channel_layer.group_send)(f"user_{photo.author.id}", message)


def notify_photo_deleted(photo):
    channel_layer = get_channel_layer()

    message = {
        "type": "inform",
        "text": f"Фотография {photo.title} была отправлена на удаление. "
        f"Ваши комментарии к фотографии скоро будут удалены",
    }

    async_to_sync(channel_layer.group_send)(f"user_{photo.author.id}", message)


def broadcast_message(message):
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        "global_notifications", {"type": "inform", "text": message}
    )

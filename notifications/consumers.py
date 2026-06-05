from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationsConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_group_name = None
        self.global_group_name = None

    async def connect(self):
        user = self.scope["user"]

        if user.is_anonymous:
            await self.close()
            return

        self.user_group_name = f"user_{user.id}"
        self.global_group_name = "global_notifications"

        await self.channel_layer.group_add(self.user_group_name, self.channel_name)
        await self.channel_layer.group_add(self.global_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        if self.user_group_name:
            await self.channel_layer.group_discard(
                self.user_group_name, self.channel_name
            )
        if self.global_group_name:
            await self.channel_layer.group_discard(
                self.global_group_name, self.channel_name
            )

    async def inform(self, event):
        await self.send(text_data=event["text"])

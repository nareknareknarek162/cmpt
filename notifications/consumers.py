from channels.generic.websocket import WebsocketConsumer


class NotificationsConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.send(text_data="hi it works")

    def disconnect(self, close_code):
        pass

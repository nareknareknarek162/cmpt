from django.urls import re_path

from .consumers import NotificationsConsumer

ws_urlpatterns = [
    re_path("ws/notifications/", NotificationsConsumer.as_asgi()),
]

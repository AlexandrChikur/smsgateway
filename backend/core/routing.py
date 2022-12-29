
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("api/ws/messages/", consumers.MessageConsumer.as_asgi()),
]
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from websocket_message.consumers import MessageConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("ws://", MessageConsumer),
    ])
})
# application = ProtocolTypeRouter({
#     "wsmessage": MessageConsumer,
# })
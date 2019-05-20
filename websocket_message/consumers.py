import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.consumer import SyncConsumer


class MessageConsumer(WebsocketConsumer):

    def connect(self):
        async_to_sync(self.channel_layer.group_add)("deviation_message", self.channel_name)
        print('channel_name______{}'.format(self.channel_name))
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)("deviation_message", self.channel_name)
        pass

    def websocket_receive(self, text_data):
        async_to_sync(self.channel_layer.group_send)(
            "deviation_message",
            {
                "type": "deviation_message",
                "text": text_data,
            },
        )

    def deviation_message(self, event):
        self.send(text_data=json.dumps({
            'message': event["text"]
        }))

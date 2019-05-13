from channels.consumer import SyncConsumer


class MessageConsumer(SyncConsumer):

    def websocket_message(self, message):

        self.send({
            "type": "websocket.message",
            "text": "You said: %s" % message["text"],
        })

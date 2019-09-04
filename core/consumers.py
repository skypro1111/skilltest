from channels.generic.websocket import AsyncWebsocketConsumer
import json


class FormsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['group_name']
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        print(text_data)
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'broadcast_message',
                'message': text_data
            }
        )

    async def broadcast_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))

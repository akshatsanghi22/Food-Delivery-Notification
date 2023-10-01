import json

from channels.generic.websocket import AsyncWebsocketConsumer


# class NotificationConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
#         self.room_group_name = f"chat_{self.room_name}"

#         # Join room group
#         await self.channel_layer.group_add(self.room_group_name, self.channel_name)

#         await self.accept()

#     async def disconnect(self, close_code):
#         # Leave room group
#         await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

#     # Receive message from WebSocket
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]

#         # Send message to room group
#         await self.channel_layer.group_send(
#             self.room_group_name, {"type": "chat.message", "message": message}
#         )

#     # Receive message from room group
#     async def chat_message(self, event):
#         message = event["message"]

#         # Send message to WebSocket
#         await self.send(text_data=json.dumps({"message": message}))


#notification consumers        

# # from channels.generic.websocket import AsyncWebsocketConsumer
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer

# class NotificationConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     async def disconnect(self, close_code):
#         pass

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         user_id = data.get('user_id')
#         order_id = data.get('order_id')
#         payment_id = data.get('payment_id')
#         notification_text=data.get('notification_text')
#         message = f"New notification: User {user_id}, Order {order_id}, Payment {payment_id},text {notification_text}"
#         await self.send(text_data=json.dumps({'message': message}))


#notification

# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from channels.layers import get_channel_layer

# class NotificationConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     async def disconnect(self, close_code):
#         pass


#     async def send_notification(self, event):
#         message = event['message']

#         # Send the notification to the WebSocket client
#         await self.send(text_data=json.dumps({
#             'message': message}))


###notification

import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.template.loader import get_template

class NotificationConsumer(WebsocketConsumer):
    """
    Websocket consumer for handling notifications.
    """
    
    def connect(self):
        """
        Connects the WebSocket consumer to a group in the channel layer.
        """
        self.group_name = 'src'
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        """
        Disconnects the WebSocket connection.

        Parameters: close_code (int): The close code to send to the client.
        """
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def notify(self, event):
        """
        Send a django_notification by converting the event to JSON and sending it as text data.

        :param event: The event to be sent as a django_notification.
        :type event: Any
        """
        self.send(text_data=json.dumps(event))



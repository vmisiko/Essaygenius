from .models import Message, Room
from asgiref.sync import async_to_sync
from users.models import CustomUser
from channels.generic.websocket import WebsocketConsumer
import json

class Consumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        part = room_name.split("_")
        part_1 = CustomUser.objects.get(user=int(part[0]))
        part_2 = CustomUser.objects.get(user=int(part[1]))
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        try:
            self.Room  = Room.objects.get( room_name= self.room_group_name)
            if len(Self.Room.participants) < 2:
                # emprt room part
                self.Room.participants.add(part_1)
                self.Room.participants.add(part_2)
                self.Room.save()
        except:
            self.Room = Room.objects.create( room_name = self.room_group_name)
            self.Room.participants.add(part_1)
            self.Room.participants.add(part_2)
            self.Room.save()
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']
        receiver = text_data_json['receiver']
        
        if(receiver):
            senderInstance = CustomUser.objects.get(pk=sender['id'])
            newMessage = Message(sender=senderInstance,text=message)
            newMessage.save()

            self.Room.room.messages.add(newMessage)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender' : sender
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        print(message)

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))
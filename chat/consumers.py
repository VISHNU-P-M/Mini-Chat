from channels.generic.websocket import WebsocketConsumer
import json
from .models import *
from asgiref.sync import async_to_sync
from datetime import datetime


class ChatRoomConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        self.accept()
        
    def disconnect(self,close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        
    def receive(self,text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        receiver = data['receiver']
        user1 = User.objects.get(username=username)
        user2 = User.objects.get(id=receiver)
        print(user1,user2,datetime.now()) 
        onetoone = OneToOne.objects.get(room_name=self.room_name)
        Messages.objects.create(sender=user1,receiver=user2,onetoone=onetoone,date=datetime.now(),message=message)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username':username
                
            }
        )
        
    def chat_message(self, event):
        message = event['message']
        username = event['username']
        async_to_sync(
            self.send(text_data=json.dumps({
            'message':message,
            'username':username
            }))
        )  
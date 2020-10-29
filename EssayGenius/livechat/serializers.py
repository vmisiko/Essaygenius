from .models import Message, Room
from rest_framework import serializers
from users.serializers import UserGetSerializer


class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Message
        fields="__all__"

class RoomSerializer(serializers.ModelSerializer):
    participants = UserGetSerializer(many=True, required=False)
    messages = MessageSerializer(many=True, required=False)

    class Meta:
        model=Room
        fields="__all__"
        
    
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import CustomUser
from users.serializers import UserGetSerializer
from .serializers import MessageSerializer,RoomSerializer
from .models import Message,Room
from django.db.models import Q
from django.db.models import Count
from rest_framework import generics




@api_view(["GET",])
@permission_classes([IsAuthenticated])
def message(request, pk):
    user1 = CustomUser.objects.get(pk=pk)
    user2 = CustomUser.objects.get(pk=request.user.pk)
    all_users= CustomUser.objects.all()
    queryset = Message.objects.filter(Q(receiver=user1) | Q(sender=user2)).order_by("created_at").distinct()
    allusers = UserGetSerializer(all_users,many=True)
    current_user= UserGetSerializer(request.user)
    selected_user = UserGetSerializer(user1)
    messages = MessageSerializer(queryset.order_by('created_at'), many=True)

    json_response = {
        'users': allusers.data,
        'current_user': current_user.data ,
        'selected_user': selected_user.data,
        'messages': messages.data
    }

    return Response(json_response)

@api_view(["GET",])
@permission_classes([IsAuthenticated])
def messagelist(request):
    user= CustomUser.objects.get(pk=request.user.pk)
    rooms = Room.objects.filter(participants=user)

    for room in rooms:
        print(room)
        

    # all_users= CustomUser.objects.all()
    # queryset = Message.objects.filter(Q(receiver=user) | 
    # Q(sender=user)).order_by("created_at").select_related("sender","receiver").distinct()
    # allusers = UserGetSerializer(all_users,many=True)
    # current_user= UserGetSerializer(request.user)
    # messages = MessageSerializer(queryset, many=True)

    # roomchats1 = [mesroom.chat_room for mesroom in queryset]
    # roomchats = list(set(roomchats1))
    # rooms1 = Room.objects.filter(room__in =roomchats)
    roomserializer = RoomSerializer(rooms, many=True)    
    # print(rooms.data)
    json_response = {
        "room":roomserializer
    }

    return Response(json_response)


class MessageList(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        user= CustomUser.objects.get(pk=self.request.user.pk)
        qs = Room.objects.filter(participants=user)
        return qs


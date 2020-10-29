from django.db import models
from django.conf import settings
from users.models import CustomUser


class Message(models.Model):
    text = models.CharField(max_length=100,blank=True, null =True)
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='messages_sent', on_delete=models.CASCADE)
    

class Room(models.Model):
    participants = models.ManyToManyField(CustomUser, blank=True)
    room_name= models.TextField( blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    messages = models.ManyToManyField(Message, related_name="message",blank=True)





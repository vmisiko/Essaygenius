from django.contrib import admin
from .models import Message
from .models import Room
# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["text","created_at","sender"]
    
@admin.register(Room)
class RoomsAdmin(admin.ModelAdmin):
    list_display = ["date","room_name"]
from django.urls import path, include
from . import views

app_name = "livechat"

urlpatterns = [
    
    path("message/<int:pk>/", views.message , name = "messages"),
    # path("messagelist/", views.messagelist , name = "messageslist"),
    path("messagelist/", views.MessageList.as_view() , name = "messageslist"),


]
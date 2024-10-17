from django.urls import path
from .views import *

urlpatterns = [
    path('chat/<username>', get_or_create_chatroom, name="startchat"),
    path('chat/room/<chatroom_name>', chats, name="chatroom")
]
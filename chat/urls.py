from django.urls import path
from .views import *

urlpatterns = [
    path('chat/<username>', get_or_create_chatroom, name="startchat"),
    path('chat/room/<chatroom_name>', chats, name="chatroom"),
    path('chat/new_groupchat/', create_groupchat, name="new_groupchat"),
    path('chat/edit/<chatroom_name>', edit_chatroom, name="edit_chatroom"),
    path('chat/delete/<chatroom_name>', delete_chatroom, name="delete_chatroom")
]
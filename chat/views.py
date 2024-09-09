from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def chats(request):
    chat_group = get_object_or_404(ChatGroup, group_name='public')
    messages = chat_group.chat_messages.all()[:30]
    return render(request, 'chats.html', {'messages':messages})

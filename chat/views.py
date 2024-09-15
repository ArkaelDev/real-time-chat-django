from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

@login_required
def chats(request):
    chat_group = get_object_or_404(ChatGroup, group_name='public')
    messages = chat_group.chat_messages.all()[:30]
    form = ChatMessageForm()

    if request.htmx:
        form = ChatMessageForm(request.POST)
        if form.is_valid:
            message=form.save(commit=False)
            message.author=request.user
            message.group=chat_group
            message.save()
            context={
                'message':message,
                'user':request.user
            }
            return render(request,'message_p.html', context)
    return render(request, 'chats.html', {'messages':messages, 'form':form})

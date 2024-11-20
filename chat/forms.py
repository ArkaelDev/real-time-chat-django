from django.forms import ModelForm
from django import forms
from . models import *

class ChatMessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['body']
        widgets = {'body': forms.TextInput(attrs={
            'placeholder':'Add message',
            'class':'box-border w-full rounded-md p-4 text-black',
            'maxlength':'300','autofocus':True})}

class CreateGroup(ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['groupchat_name']
        widgets = {
            'groupchat_name': forms.TextInput(attrs={
            'placeholder':'Add group name',
            'class':'box-border w-full rounded-md p-4 text-b',
            'maxlength':'300',
            'autofous':True,
        })
        }
        
class ChatroomEdit(ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['groupchat_name']
        widgets = {
            'groupchat_name': forms.TextInput(attrs={
                'class' : 'p-4 text-xl font-bold mb-4',
                'maxlength': '300',
            })
        }
from django.forms import ModelForm
from django import forms
from . models import *

class ChatMessageForm(ModelForm):
    class Meta:
        model = Messages
        fields = ['body']
        widgets = {'body': forms.TextInput(attrs={'placeholder':'Add message','class':'box-border w-full rounded-md p-4 text-black','maxlength':'300','autofocus':True})}
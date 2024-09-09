from django.forms import ModelForm
from django import forms
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            'avatar' : forms.Select(),
            'displayname' : forms.TextInput(attrs={'placeholder':'Add display name'}),
            'info' : forms.Textarea(attrs={'rows':3,'placeholder':'Add info', 'class':'info',})
        }


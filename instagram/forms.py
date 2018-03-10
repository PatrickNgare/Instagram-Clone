from django import forms
from .models import Image,Profile,Comment


class UploadForm(forms.ModelForm):
    
    class Meta:
        model = Image
        exclude = ['user','profile','likes','comments']

class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['writer','post','timecomment',]


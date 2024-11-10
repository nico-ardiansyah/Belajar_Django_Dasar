from django import forms
from . import models

class NewPost(forms.ModelForm):
    class Meta:
        model = models.CreatePost
        fields = ['title', 'content', 'banner']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-title', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-content', 'placeholder': 'Content'}),
            'banner': forms.FileInput(attrs={'class': 'form-banner', 'placeholder': 'image'}),
        }
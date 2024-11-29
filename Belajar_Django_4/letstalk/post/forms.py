from django import forms
from . import models

class NewPost(forms.ModelForm):
    class Meta:
        model = models.CreatePost
        fields = ['content', 'banner']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-content', 'placeholder': 'Your content'}),
            'banner': forms.FileInput(attrs={'class': 'form-banner'}),
        }
        
class CommentForm(forms.ModelForm):
    comment_text = forms.CharField(widget=forms.Textarea(attrs={'class': 'fields'}))
    class Meta:
        model = models.Comment
        fields = ('comment_text',)
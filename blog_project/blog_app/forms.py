from django import forms
from . import models

# Create your forms here

class Post_Form(forms.ModelForm):
    
    class Meta():
        model = models.Post
        fields = ('author', 'title','text')

        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }


class Comment_Form(forms.ModelForm):
    
    class Meta():
        model = models.Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }




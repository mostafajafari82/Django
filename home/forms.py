from django import forms
from .models import Comment

class SearchHomeForm(forms.Form):

    query = forms.CharField(max_length=100, label="search")


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['text']
from django import forms
from articleapp.models import Article
from django.forms import ModelForm


class ArticleCreationForm(ModelForm):

    content = forms.Textarea

    class Meta:
        model = Article
        fields = ["title", "image", "content", "project"]
        widgets = {
            'content': forms.Textarea(attrs={"class": 'editable'}),
        }
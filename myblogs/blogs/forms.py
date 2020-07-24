from django.forms import ModelForm
from .models import Blog
from django import forms

class BlogModelForm(ModelForm):
    author_id = forms.IntegerField(widget=forms.HiddenInput,initial=1)
    class Meta:
        model = Blog
        fields = ['title','body']
        
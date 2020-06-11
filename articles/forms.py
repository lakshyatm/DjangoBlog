from django import forms
from . import models
from .models import Article

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title','body','slug','thumb']

#class CommentForm(forms.ModelForm):

#    class Meta:
##        fields = ('author', 'text',)

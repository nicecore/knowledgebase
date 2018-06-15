from django import forms
from django.contrib.auth.models import User
from .models import Article, Category

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'slug']


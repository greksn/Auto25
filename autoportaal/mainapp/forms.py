from django import forms
from .models import Article, Post

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class CarPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
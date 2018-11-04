from django import forms
from .models import Article, Thread, ForumPost, Post


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class CarPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = '__all__'


class ForumPostForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = '__all__'

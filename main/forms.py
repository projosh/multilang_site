from django import forms
from .models import Article


class BlogArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'publication_date']
        
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'publication_date']


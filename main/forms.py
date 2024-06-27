from django import forms
from .models import articles_de_blog


class BlogArticleForm(forms.ModelForm):
    class Meta:
        model = articles_de_blog
        fields = ['title', 'content', 'publication_date']

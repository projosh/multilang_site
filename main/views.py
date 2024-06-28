
from django.shortcuts import render
from django.utils.translation import gettext as _

from main.models import Article

# Create your views here.

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})


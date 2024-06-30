
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext as _
from main.models import Article
from .forms import ArticleForm 

# Create your views here.

# list article
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})

# detail article

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'main/article_detail.html', {'article': article})

# delete article
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'main/delete_article.html', {'article': article})

def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')  # Rediriger vers la liste des articles après ajout
    else:
        form = ArticleForm()

    return render(request, 'main/add_article.html', {'form': form})

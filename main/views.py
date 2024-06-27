
from django.shortcuts import render
from .models import articles_de_blog




# Create your views here.
def article_list(request):
    articles = articles_de_blog.objects.all()
    context = context = {
        "articles": articles,
        "message": "salut"
    }
    return render(request, 'main/article_list.html',context)


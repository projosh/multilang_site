from django.shortcuts import render, get_object_or_404, redirect
from .models import articles_de_blog
from .forms import BlogArticleForm
from django.shortcuts import render, get_object_or_404, redirect



# Create your views here.

def article_list(request):
    articles = articles_de_blog.objects.all()
    return render(request, 'main/article_list.html', {articles : articles})

def article_edit(request, pk):
    article = get_object_or_404(articles_de_blog, pk=pk)
    if request.method == 'POST':
        form = BlogArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = BlogArticleForm(instance=article)
    return render(request, 'main/article_edit.html', {'form': form})
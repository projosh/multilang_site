
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext as _
from main.models import Article
from .forms import ArticleForm 
import openai

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

# create article
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'main/article_form.html', {'form': form})

def article_update(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'main/article_form.html', {'form': form})

def chatbot_view(request):
    if request.method == 'POST':
        user_message = request.POST['message']

        # Generate response using ChatGPT
        completion = openai.Completion(engine="text-davinci-003", prompt=user_message, max_tokens=150)
        response = completion.choices[0].text.strip()

        # Return JSON response
        return HttpResponse(response, content_type='application/json')
    
    def chatbot_template(request):
        return render(request, 'main/chatbot_template.html')
  

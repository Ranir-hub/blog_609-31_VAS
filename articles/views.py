from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from articles.models import Article
from . import forms

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles' : articles})

def article_item(request, slug):
    articles = Article.objects.all().order_by('date')
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_item.html', {'article': article, 'articles' : articles})

@login_required(login_url = 'accounts:login')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('homepage')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})
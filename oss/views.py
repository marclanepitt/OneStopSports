from django.shortcuts import render
from blogs.models import Article

def homeview(request):
    latest_article_list = Article.objects.order_by('-date_published')[:20]
    trending_article_list = Article.objects.order_by('vote_total')[:5]
    context = {'latest_article_list': latest_article_list,'trending_article_list':trending_article_list}
    return render(request, 'index.html', context)

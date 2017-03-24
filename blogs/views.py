from django.shortcuts import render, get_object_or_404
from .models import Article


def detail(request,slug):
    article = get_object_or_404(Article,slug=slug)
    return render(request,'detail.html',{article,'article'})

def FootballView(request):
    football_article_list = Article.objects.filter(category = 'football')
    return render(request,'football.html',{football_article_list, 'articles'})


def BasketballView(request):
    football_article_list = Article.objects.filter(category='basketball')
    return render(request, 'basketball.html', {football_article_list, 'articles'})


def BaseballView(request):
    football_article_list = Article.objects.filter(category='baseball')
    return render(request, 'baseball.html', {football_article_list, 'articles'})


def SoccerView(request):
    football_article_list = Article.objects.filter(category='soccer')
    return render(request, 'soccer.html', {football_article_list, 'articles'})


def HockeyView(request):
    football_article_list = Article.objects.filter(category='hockey')
    return render(request, 'hockey.html', {football_article_list, 'articles'})


def CollegeView(request):
    football_article_list = Article.objects.filter(category='college')
    return render(request, 'college.html', {football_article_list, 'articles'})


def OtherView(request):
    football_article_list = Article.objects.filter(category='other')
    return render(request, 'other.html', {football_article_list, 'articles'})

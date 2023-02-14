from django.http import HttpResponse
from django.shortcuts import render
from .models import Page, News

def page_list(request, slug=""):
   pages = Page.objects.filter(slug__icontains=slug).all()

   return render(request, "pages.html", {"pages" : pages})

def news_list(request):
   news_list = News.objects.all()

   return render(request, "news.html", {"news_list" : news_list})

def news_detail(request, slug):
   news = News.objects.filter(slug=slug).first()

   return render(request, "news_detail.html", {"news" : news})
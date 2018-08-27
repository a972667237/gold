#coding: utf-8
from django.shortcuts import render, get_object_or_404
from .models import Comment_article, Encyclopedia_article, Announcement_article

# Create your views here.

def index(requests):
    comment = Comment_article.objects.all()[:5]
    encyclopedia = Encyclopedia_article.objects.all()[:5]
    announcement = Announcement_article.objects.all()[:3]
    return render(requests, 'main.html', locals())

def comment(requests):
    article = Comment_article.objects.all()
    final = "利汇金评"
    final_type = 1
    return render(requests, 'list.html', locals())

def encyclopedia(requests):
    article = Encyclopedia_article.objects.all()
    final = "利汇百科"
    final_type = 2
    return render(requests, 'list.html', locals())

def announcement(requests):
    article = Announcement_article.objects.all()
    final = "利汇公告"
    final_type = 3
    return render(requests, 'list.html', locals())

def detail(requests):
    pk = requests.GET.get('id', 1)
    t = requests.GET.get('type', 1)
    pk = int(pk)
    final_type = int(t)
    middle = None
    search = None
    middle_url = None
    if final_type == 2:
        search = Encyclopedia_article
        middle = "利汇百科"
        middle_url = 'encyclopedia_list'
    elif final_type == 3:
        search = Announcement_article
        middle = "利汇公告"
        middle_url = 'announcement_list'
    else:
        search = Comment_article
        middle = "利汇金评"
        middle_url = 'comment_list'
    article = get_object_or_404(search, pk=pk)
    final = article.title
    return render(requests, 'detail.html', locals())

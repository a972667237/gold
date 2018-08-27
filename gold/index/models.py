# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.
class Article(models.Model):
    title = models.CharField(u'title', max_length=100)
    content = UEditorField(u'content', max_length=200000)
    description = models.TextField(u'description', max_length=10000)
    date = models.DateField(u'create_date', auto_now_add=True, editable=True)
    author = models.CharField(u'author', max_length=100)
    time = models.DateField(u'publish_time')
    class Meta:
        abstract = True
    def __unicode__(self):
        return self.title

class Comment_article(Article):
    class Meta:
        verbose_name = 'comment 评论'
        verbose_name_plural = verbose_name

class Encyclopedia_article(Article):
    class Meta:
        verbose_name = 'encyclopedia 百科'
        verbose_name_plural = verbose_name

class Announcement_article(Article):
    class Meta:
        verbose_name = 'announcement 公告'
        verbose_name_plural = verbose_name

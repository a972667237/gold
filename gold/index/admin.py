from django.contrib import admin
from .models import Comment_article, Encyclopedia_article, Announcement_article

# Register your models here.
admin.site.register(Comment_article)
admin.site.register(Encyclopedia_article)
admin.site.register(Announcement_article)

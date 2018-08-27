from django.contrib import admin
from django.conf.urls import url
from django.http import HttpResponseRedirect
from .views import index, comment, encyclopedia, detail, announcement

urlpatterns = [
    url(r'^comment_list', comment),
    url(r'^encyclopedia_list', encyclopedia),
    url(r'^announcement_list', announcement),
    url(r'^detail', detail),
    url(r'^about', lambda x: HttpResponseRedirect('/detail?id=1&type=1')),
    url(r'^analyze', lambda x: HttpResponseRedirect('/comment_list')),
    url(r'^situation', lambda x: HttpResponseRedirect('/encyclopedia_list')),
    url(r'^notice', lambda x: HttpResponseRedirect('/detail?id=3&type=1')),
    url(r'^advantage', lambda x: HttpResponseRedirect('/detail?id=4&type=1')),
    url(r'^safe', lambda x: HttpResponseRedirect('/detail?id=5&type=1')),
    url(r'^process', lambda x: HttpResponseRedirect('/detail?id=2&type=1')),
    url(r'^manage', lambda x: HttpResponseRedirect('http://v.sprd888.com/default/UserPwdLogin.aspx?agent=20035')),
    url(r'^simulation', lambda x: HttpResponseRedirect('http://moni.jo72.cn')),
    url(r'^login', lambda x: HttpResponseRedirect('http://v.sprd888.com/Default/UserPwdLogin.aspx?agent=20035')),
    url(r'^signup', lambda x: HttpResponseRedirect('http://v.sprd888.com/default/UserRegister.aspx?agent=20035')),
    url(r'^$', index),
]

from django.conf.urls import patterns, url

from essay import views
from mblog import settings

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^type/(?P<tname>[\w_-]+)/$', views.types, name='types'),
    url(r'^time/(?P<ym>.+)/$', views.display, name='display'),
    url(r'^essay/(?P<id>\d+)/$', views.essay_detail, name='essay_detail'),
    url(r'^comments/(?P<id>\d+)/$', views.comments, name='comments'),
    url(r'^comments/add/$', views.comments_add, name='comments_add'),
    url(r'^about$', views.contact, name='contact'),
)
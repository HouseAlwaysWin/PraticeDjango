from django.conf.urls import include, url
from .views import (post_list,post_detail)

urlpatterns = [
    url(r'^$',
        post_list,
        name='blog_post_list'),
    url(r'^(?P<year>\d{4})/'
        r'(?P<month>\{1,2})/'
        r'(?P<slug>[\w\-]+)/$',
        post_detail,
        name='blog_post_detail'),
    ]

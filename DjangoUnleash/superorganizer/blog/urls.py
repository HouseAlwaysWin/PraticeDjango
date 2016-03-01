from django.conf.urls import include, url
from .views import (PostList,
                    post_detail)

urlpatterns = [
    url(r'^$',
        PostList.as_view(),
        {'paretn_template':'base.html'},
        name='blog_post_list'),
    
    url(r'^(?P<year>\d{4})/'
        r'(?P<month>\{1,2})/'
        r'(?P<slug>[\w\-]+)/$',
        post_detail,
        {'paretn_template':'base.html'},
        name='blog_post_detail'),
    ]

from django.conf.urls import url

from .views import (tag_list,
                    tag_detail,
                    startup_list,
                    startup_detail,
                    TagCreate,
                    TagUpdate,
                    StartupCreate,
                    StartupUpdate,
                    NewsLinkCreate,
                    NewsLinkUpdate)

urlpatterns = [
    url(r'tag/$',
        tag_list,
        name='organizer_tag_list'),

    url(r'^tag/create/$',
        TagCreate.as_view(),
        name='organizer_tag_create'),

    url(r'^tag/(?P<slug>[\w\-]+)/$',
        tag_detail,
        name='organizer_tag_detail'),

    url(r'^tag/(?P<slug>[\w\-]+)/update/$',
        TagUpdate.as_view(),
        name='organizer_tag_update'),

    url(r'^startup/$',
        startup_list,
        name='organizer_startup_list'),

    url(r'^startup/create/$',
        StartupCreate.as_view(),
        name='organizer_startup_create'),

    url(r'startup/(?P<slug>[\w\-]+)/$',
        startup_detail,
        name='organizer_startup_detail'),

    url(r'startup/(?P<slug>[\w\-]+)/update/$',
        StartupUpdate.as_view(),
        name='organizer_startup_update'),

    url(r'^newslink/create/$',
        NewsLinkCreate.as_view(),
        name='organizer_newslink_create'),

    url(r'^newlink/update/(?P<pk>\d+)/$',
        NewsLinkUpdate.as_view(),
        name='organizer_newslink_update'),
    ]

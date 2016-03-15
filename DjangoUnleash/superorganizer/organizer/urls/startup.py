from django.conf.urls import url

from organizer.views import (StartupList,
                             StartupDetail,
                             StartupCreate,
                             StartupUpdate,
                             StartupDelete,
                             NewsLinkCreate,
                             NewsLinkDelete,
                             NewsLinkUpdate)



urlpatterns = [
    url(r'^$',
        StartupList.as_view(),
        name='organizer_startup_list'),

    url(r'^create/$',
        StartupCreate.as_view(),
        name='organizer_startup_create'),

    url(r'^(?P<slug>[\w\-]+)/$',
        StartupDetail.as_view(),
        name='organizer_startup_detail'),

    url(r'^(?P<slug>[\w\-]+)/update/$',
        StartupUpdate.as_view(),
        name='organizer_startup_update'),

    url(r'^(?P<slug>[\w\-]+)/delete/$',
        StartupDelete.as_view(),
        name='organizer_startup_delete'),

    url(r'^(?P<startup_slug>[\w\-]+)/'
        r'add_article_link/$',
        NewsLinkCreate.as_view(),
        name='organizer_newslink_create'),

    url(r'^(?P<startup_slug>[\w\-]+)/'
        r'(?P<newslink_slug>[\w\-]+)/'
        r'delete/$',
        NewsLinkDelete.as_view(),
        name='organizer_newslink_delete'),

    url(r'^(?P<startup_slug>[\w\-]+)/'
        r'(?P<newslink_slug>[\w\-]+)/'
        r'update/$',
        NewsLinkUpdate.as_view(),
        name='organizer_newslink_update'),

]

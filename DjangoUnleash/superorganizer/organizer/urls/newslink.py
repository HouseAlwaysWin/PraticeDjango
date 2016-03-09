from django.conf.urls import url

from organizer.views import (NewsLinkCreate,
                   NewsLinkUpdate,
                   NewsLinkDelete)

urlpatterns = [
    url(r'^create/$',
        NewsLinkCreate.as_view(),
        name='organizer_newslink_create'),

    url(r'^update/(?P<pk>\d+)/$',
        NewsLinkUpdate.as_view(),
        name='organizer_newslink_update'),

    url(r'^delete/(?P<pk>\d+)/$',
        NewsLinkDelete.as_view(),
        name='organizer_newslink_delete'),
]

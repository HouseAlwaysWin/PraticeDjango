from django.conf.urls import url

from organizer.views import (
    TagList,
    TagDetail,
    TagCreate,
    TagUpdate,
    TagDelete)


urlpatterns = [
    
    url(r'^$',
        TagList.as_view(),
        name='organizer_tag_list'),

    url(r'^create/$',
        TagCreate.as_view(),
        name='organizer_tag_create'),

    url(r'^(?P<slug>[\w\-]+)/$',
        TagDetail.as_view(),
        name='organizer_tag_detail'),

    url(r'^(?P<slug>[\w\-]+)/update/$',
        TagUpdate.as_view(),
        name='organizer_tag_update'),

    url(r'^(?P<slug>[\w\-]+)/delete/$',
        TagDelete.as_view(),
        name='organizer_tag_delete'),
]

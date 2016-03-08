from django.conf.urls import url

from organizer.views import (tag_list,
                    tag_detail,
                    TagCreate,
                    TagUpdate,
                    TagDelete)


urlpatterns = [
    url(r'^tag/$',
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

    url(r'^tag/(?P<slug>[\w\-]+)/delete/$',
        TagDelete.as_view(),
        name='organizer_tag_delete'),
]

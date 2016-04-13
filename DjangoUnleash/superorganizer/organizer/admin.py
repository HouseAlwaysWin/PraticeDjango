from django.contrib import admin

from .models import NewsLink, Startups, Tag


admin.site.register(NewsLink)
admin.site.register(Startups)
admin.site.register(Tag)

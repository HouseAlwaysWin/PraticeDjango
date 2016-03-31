from django.shortcuts import get_object_or_404
from .models import Startups ,NewsLink



class NewsLinkFormMixin:

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method in ('POST','PUT'):
            self.startup = get_object_or_404(
                Startup,slug__iexact=self.kwargs.get(
                    self.startup_slug_url_kwarg))
            data = kwargs['data'].copy()
            data.update({'startup':self.startup})
            kwargs['data'] = data

        return kwargs

class NewsLinkGetObjectMixin:

    def get_object(self, queryset=None):
        startup_slug = self.kwargs.get(
            self.startup_slug_url_kwarg)
        newslink_slug = self.kwargs.get(
            self.slug_url_kwarg)
        return get_object_or_404(
            NewsLink,
            slug__iexact=newslink_slug,
            startup__slug__iexact=startup_slug)

class PageLinksMixin:
    page_kwarg = 'page'

    
    def _page_urls(self, page_number):
        return "?{pkw}={n}".format(
            pkw=self.page_kwarg,
            n=page_number)

    def previous_page(self, page):
        if (page.has_previous()
            and page.number > 2):
            return self._page_urls(
                page.previous_page_number())
        return None

    def next_page(self, page):
        last_page = page.paginator.num_pages
        if (page.has_next() and page.number < last_page -1):
            return self._page_urls(
                page.next_page_number())
        return None

    def first_page(self, page):
        #don't show on first page
        if page.number > 1:
            return self._page_urls(1)
        return None

    def last_page(self, page):
        last_page = page.paginator.num_pages
        if page.number < last_page:
            return self._page_urls(last_page)
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(
            **kwargs)
        page = context.get('page_obj')
        if page is not None:
            context.update({
                'first_page_url':self.first_page(page),
                'previous_page_url':self.previous_page(page),
                'next_page_url':self.next_page(page),
                'last_page_url':self.last_page(page),
            })
        return context

class StartupContextMixin:
    startup_slug_url_kwarg = 'startup_slug'
    startup_context_object_name = 'startups'

    def get_context_data(self, **kwargs):
        if hasattr(self,'startups'):
            context = {
                self.startup_context_object_name: self.startups,}
        else:
            startup_slug = self.kwargs.get(
                self.startup_slug_url_kwarg)
            startup = get_object_or_404(
                Startups,
                slug__iexact=startup_slug)
            
            context = {
                self.startup_context_object_name:startup,
            }
            context.update(kwargs)
             
        return super().get_context_data(**context)

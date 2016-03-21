from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  DeleteView)
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import (Paginator,
                                   EmptyPage,
                                   PageNotAnInteger)
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import  user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth import PermissionDenied

from .forms import (TagForm,
                    StartupForm,
                    NewsLinkForm)
from .models import (Tag,
                     Startups,
                     NewsLink)
from core.utils import UpdateView

from .utils import (PageLinksMixin,
                    NewsLinkGetObjectMixin,
                    NewsLinkFormMixin,
                    StartupContextMixin)

class TagList(PageLinksMixin, ListView):
    paginate_by = 5
    model = Tag

class TagDetail(DetailView):
    model = Tag



class TagCreate(CreateView):
    form_class = TagForm
    model = Tag

    @method_decorator(
        permission_required(
            'organizer.add_tag',
            raise_exception=True
        ))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(
            request, *args, **kwargs)


class TagUpdate(UpdateView):
    form_class = TagForm
    model = Tag


class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy(
        'organizer_tag_list')
    template_name = ('organizer/tag_confirm_delete.html')



class StartupList(PageLinksMixin, ListView):
    model = Startups
    paginate_by = 5
    template_name = 'organizer/startup_list.html'

class StartupDetail(DetailView):
    model = Startups
    template_name = 'organizer/startup_detail.html'


class StartupCreate(CreateView):
    form_class = StartupForm
    model = Startups
    template_name = 'organizer/startup_form.html'

class StartupUpdate(UpdateView):
    form_class = StartupForm
    model = Startups
    template_name = 'organizer/startup_form_update.html'

class StartupDelete(DeleteView):
    model = Startups
    success_url = reverse_lazy(
        'organizer_startup_list')
    template_name = ('organizer/startup_confirm_delete.html')


class NewsLinkCreate(NewsLinkFormMixin,
                     NewsLinkGetObjectMixin,
                     StartupContextMixin,
                     CreateView):
    
    form_class = NewsLinkForm
    model = NewsLink

    def get_initial(self):
        startup_slug = self.kwargs.get(
            self.startup_slug_url_kwarg)
        self.startup = get_object_or_404(
            Startup, slug__iexact=startup_slug)
        initial = {
            self.startup_context_object_name:
            self.startup,
        }
        initial.update(self.initial)

        return initial


class NewsLinkUpdate(NewsLinkGetObjectMixin,
                     StartupContextMixin,
                     UpdateView):
    
    form_class = NewsLinkForm
    model = NewsLink
    slug_url_kwarg = 'newslink_slug'

    
class NewsLinkDelete(StartupContextMixin,DeleteView):
    model = NewsLink
    slug_url_kwarg = 'newslink_slug'

    def get_success_url(self):
        return (self.object.startup.get_absolute_url())

from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  DeleteView)
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import (Paginator,
                                   EmptyPage,
                                   PageNotAnInteger)

from .forms import (TagForm,
                    StartupForm,
                    NewsLinkForm)
from .models import (Tag,
                     Startups,
                     NewsLink)
from core.utils import UpdateView

from .utils import PageLinksMixin

class TagList(PageLinksMixin, ListView):
    paginate_by = 5
    model = Tag

class TagDetail(DetailView):
    model = Tag



class TagCreate(CreateView):
    form_class = TagForm
    model = Tag


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


class NewsLinkCreate(CreateView):
    form_class = NewsLinkForm
    model = NewsLink


class NewsLinkUpdate(UpdateView):
    form_class = NewsLinkForm
    model = NewsLink

    
class NewsLinkDelete(DeleteView):
    model = NewsLink

    def get_success_url(self):
        return (self.object.startup.get_absolute_url())

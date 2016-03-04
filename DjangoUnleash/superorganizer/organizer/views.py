from django.shortcuts import (render,
                              get_object_or_404,
                              redirect)
from django.views.generic import View
from .forms import (TagForm,
                    StartupForm,
                    NewsLinkForm)
from .models import (Tag,
                     Startups)
from .utils import ObjectCreateMixin

def tag_list(request):
    return render(
        request,
        'organizer/tag_list.html',
        {'tag_list':Tag.objects.all()})

def tag_detail(request, slug):
    tag = get_object_or_404(
       Tag, slug__iexact=slug)
    return render(
        request,
        'organizer/tag_detail.html',
        {'tag':tag})

class TagCreate(ObjectCreateMixin,View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'

def startup_list(request):
    return render(
        request,
        'organizer/startup_list.html',
        {'startups_list':Startups.objects.all()})

def startup_detail(request, slug):
    startup = get_object_or_404(
        Startups, slug__iexact=slug)
    return render(
        request,
        'organizer/startup_detail.html',
        {'startup':startup})

class StartupCreate(ObjectCreateMixin,View):
    form_class = StartupForm
    template_name = 'organizer/startup_form.html'


class NewsLinkCreate(ObjectCreateMixin,View):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form.html'

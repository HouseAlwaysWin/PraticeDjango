from django.shortcuts import (render,
                              get_object_or_404,
                              redirect)
from django.views.generic import View
from .forms import (TagForm,
                    StartupForm,
                    NewsLinkForm)
from .models import Tag, Startups

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

class TagCreate(View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form':self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():    
            new_tag = bound_form.save()
            return redirect(new_tag)
        else:
            return render(
                request,
                self.template_name,
                {'form':bound_form})

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

class StartupCreate(View):
    form_class = StartupForm
    template_name = 'organizer/startup_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form':self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_startup = bound_form.save()
            return redirect(new_startup)
        else:
            return render(
                request,
                self.template_name,
                {'form':bound_form})

class NewsLinkCreate(View):
    form_class = NewsLinkForm
    template_name = 'organizer/newslink_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form':self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_newslink = bound_form.save()
            return redirect(new_newslink)
        else:
            return render(
                request,
                self.template_name,
                {'form':bound_form})

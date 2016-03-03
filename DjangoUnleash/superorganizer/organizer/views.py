from django.shortcuts import (render,
                              get_object_or_404,
                              redirect)

from .forms import TagForm
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

def tag_create(request):
    #Verified method whether POST or GET
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():     # if form is valid then save data or render template
            new_tag = form.save()
            return redirect(new_tag)
    else:                       # Get method or others
        form = TagForm()
        return render(
            request,
            'organizer/tag_form.html',
            {'form':form})

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
        {'startups_detail':startup})



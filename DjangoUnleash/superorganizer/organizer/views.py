from django.shortcuts import render
from django.http.response import (HttpResponse, Http404)
from django.template import Context,loader
from .models import Tag

def homepage(request):
    tag_list = Tag.objects.all()
    template = loader.get_template('organizer/tag_list.html')
    context = Context({'tag_list':tag_list})
    return HttpResponse(template.render(context))

def tag_detail(request, slug):
    try:
        tag = Tag.objects.get(slug__iexact=slug)
    except Tag.DoesNotExist:
        raise Http404
    template = loader.get_template('organizer/tag_detail.html')
    context = Context({'tag':tag})
        
    return HttpResponse(template.render(context))

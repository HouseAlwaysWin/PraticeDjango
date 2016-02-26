from django.shortcuts import (render, get_object_or_404)
from django.http.response import HttpResponse
from django.template import Context,loader
from .models import Tag

def homepage(request):
    tag_list = Tag.objects.all()
    template = loader.get_template('organizer/tag_list.html')
    context = Context({'tag_list':tag_list})
    return HttpResponse(template.render(context))

def tag_detail(request, slug):
    tag = get_object_or_404(
        slug__iexact=slug)
    template = loader.get_template('organizer/tag_detail.html')
    context = Context({'tag':tag})
        
    return HttpResponse(template.render(context))

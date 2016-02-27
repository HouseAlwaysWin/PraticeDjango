from django.shortcuts import (render_to_response,
                              get_object_or_404)

from .models import Tag

def homepage(request):
    return render_to_response(
        'organizer/tag_list.html',
        {'tag_list':Tag.object.all()})

def tag_detail(request, slug):
    tag = get_object_or_404(
        slug__iexact=slug)
    return render_to_response(
        'organizer/tag_detail.html',
        {'tag':tag})

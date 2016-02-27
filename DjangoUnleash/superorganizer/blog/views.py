from django.shortcuts import render
from ..models import Post

def blog_post(request):
    return render(
        request,
        'blog/post_list.html',
        {'post_list':Post.objects.all()})

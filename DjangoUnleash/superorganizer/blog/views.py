from django.shortcuts import (render,
                              get_object_or_404,
                              redirect)
from django.views.generic import (View,
                                  CreateView,
                                  ArchiveIndexView,
                                  YearArchiveView,
                                  MonthArchiveView,
                                  DeleteView,
                                  DetailView)
from django.views.decorators.http import require_http_methods
from django.core.urlresolvers import reverse_lazy

from .forms import PostForm
from .models import Post
from .utils import PostGetMixin
from core.utils import UpdateView

class PostDetail(PostGetMixin, DetailView):
    model = Post

class PostCreate(CreateView):
    form_class = PostForm
    model = Post

class PostList(ArchiveIndexView):
    allow_empty = True
    allow_future = True
    context_object_name = 'post_list'
    date_field = 'pub_date'
    make_object_list = True
    model = Post
    paginate_by = 5
    template_name = 'blog/post_list.html'

class PostUpdate(PostGetMixin, UpdateView):
    form_class = PostForm
    model = Post

    
class PostDelete(PostGetMixin, DeleteView):
    model = Post
    success_url = reverse_lazy(
        'blog_post_list')
    

class PostArchiveYear(YearArchiveView):
    model = Post
    date_field = 'pub_date'
    make_object_list = True

class PostArchiveMonth(MonthArchiveView):
    model = Post
    date_field = 'pub_date'
    month_format = '%m'

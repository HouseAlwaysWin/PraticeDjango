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
from .utils import (DateObjectMixin,
                    AllowFuturePermissionMixin,
                    PostFormValidMixin)
from core.utils import UpdateView
from user.decorators import require_authenticated_permission


class PostDetail(DateObjectMixin, DetailView):

    date_field = 'pub_date'
    model = Post
    
@require_authenticated_permission(
    'blog.create_post')
class PostCreate(PostFormValidMixin,CreateView):
    form_class = PostForm
    model = Post

class PostList(AllowFuturePermissionMixin,ArchiveIndexView):
    allow_empty = True

    context_object_name = 'post_list'
    date_field = 'pub_date'
    make_object_list = True
    model = Post
    paginate_by = 5
    template_name = 'blog/post_list.html'
    
@require_authenticated_permission(
    'blog.change_post')
class PostUpdate(PostFormValidMixin,DateObjectMixin, UpdateView):

    date_field = 'pub_date'
    form_class = PostForm
    model = Post

@require_authenticated_permission(
    'blog.delete_post')
class PostDelete(DateObjectMixin, DeleteView):

    date_field = 'pub_date'
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

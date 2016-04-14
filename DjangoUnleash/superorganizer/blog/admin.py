from django.contrib import admin
from django.db.models import Count
from datetime import datetime

from .models import Post



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_filter = ('pub_date',)
    list_display = ('title','pub_date','tag_count')
    search_fields = ('title','text')
    prepopulated_fields = {'slug':('title',)}
    filter_horizontal = ('tags','startups',)
    ## form view
    # fieldsets = (
    #     (None, {
    #         'fields': (
    #             'title','slug','author','text',
    #             )}),
    #     ('Related', {
    #         'fields':(
    #             'tags','startups')}),
    #     )


    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.has_perms(
                'view_future_post'):
            queryset = queryset.filter(
                pub_date__lte=datetime.now())
        
        return queryset.annotate(
            tag_number=Count('tags'))
    
    def tag_count(self,post):
        return post.tags.count()
    tag_count.short_description = 'Number of Tags'
    tag_count.admin_order_field = 'tag_number'
    

    



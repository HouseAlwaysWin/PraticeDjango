from django.contrib import admin

from .models import Post



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_filter = ('pub_date',)
    list_display = ('title','pub_date','tag_count')
    search_fields = ('title','text')
    prepopulated_fields = {'slug':('title',)}
    filter_horizontal = ('tags','startups',)

    # form view
    # fieldsets = (
    #     (None, {
    #         'fields': (
    #             'title','slug','author','text',
    #             )}),
    #     ('Related', {
    #         'fields':(
    #             'tags','startups')}),
    #     )


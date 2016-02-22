from django.db import models
from organizer.models import Tag,Startups

class Post(models.Model):

    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63,
                            help_text='A label for URL config.',
                            unique_for_month='pub_date')
    text = models.TextField()
    pub_date = models.DateField('date published',
                                auto_now_add=True)
    tags = models.ManyToManyField(Tag,
                                  related_name='blog_posts')
    startups = models.ManyToManyField(Startups,
                                      related_name='blog_posts')

    def __str__(self):
        return "{}:{}".format(self.title,
                              self.pub_date.strftime('%Y-%m-%d'))
    class Meta:
        verbose_name = 'blog_post'
        ordering = ['-pub_date','title']
        get_latest_by = 'pub_date'

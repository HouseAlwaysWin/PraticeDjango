from django.db import models
from django.core.urlresolvers import reverse

class Tag(models.Model):

    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31,
                            unique=True,
                            help_text='A label for URL config.')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name.title()


    def get_absolute_url(self):
        return reverse('organizer_tag_detail',
                       kwargs={'slug':self.slug})
    def get_update_url(self):
        return reverse('organizer_tag_update',
                       kwargs={'slug':self.slug})

class Startups(models.Model):

    name = models.CharField(max_length=31, db_index=True)
    slug = models.SlugField(max_length=31,
                            unique=True,
                            help_text='A label for URL config.')
    description = models.TextField()
    founded_date = models.DateField('date founded')
    contact = models.EmailField(max_length=255)
    website = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('organizer_startup_detail',
                       kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('organizer_startup_update',
                       kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'

class NewsLink(models.Model):

    title = models.CharField(max_length=63)
    pub_date = models.DateField('date published')
    link = models.URLField(max_length=255)
    startup = models.ForeignKey(Startups)

    def __str__(self):
        return "{}:{}".format(self.startup,
                              self.title)

    def get_absolute_url(self):
        return self.startup.get_absolute_url()

    def get_update_url(self):
        return reverse(
            'organizer_newslink_update',
            kwarg={'pk':self.pk})
    class Meta:
        verbose_name = "news article"

        ordering = ['-pub_date']
        get_latest_by = 'pub_date'

from django.db import models

class Tag(models.Model):

    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31,
                            unique=True,
                            help_text='A label for URL config.')


class Startups(models.Model):

    name = models.CharField(max_length=31, db_index=31)
    slug = models.SlugField(max_length=31,
                            unique=True,
                            help_text='A label for URL config.')
    description = models.TextField()
    founded_date = models.DateField('date founded')
    contact = models.EmailField(max_length=255)
    website = models.URLField(max_length=255)
    tags = models.ManyToManyFiedl(Tag)

class NewsLink(models.Model):

    title = models.CharField(max_length=63)
    pub_date = models.DateField('date published')
    link = models.URLField(max_length=255)
    startup = models.ForeignKey(Startup)

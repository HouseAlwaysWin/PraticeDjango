from django.db import models

class Tag(models.Model):

    name = models.CharField(max_length=31)
    slug = models.SlugField()
    #startups = models.ManyToManyField(Startups)

class Startups(models.Model):

    name = models.CharField(max_length=31)
    slug = models.SlugField()
    description = models.TextField()
    founded_date = models.DateField()
    contact = models.EmailField()
    website = models.URLField()
    tags = models.ManyToManyFiedl(Tag)

class NewsLink(models.Model):

    title = models.CharField(max_length=63)
    pub_date = models.DateField()
    link = models.URLField()
    startup = models.ForeignKey(Startup)

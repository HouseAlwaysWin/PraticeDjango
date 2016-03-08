# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

from datetime import date

POSTS = [
  ]    



def add_post_data(apps, shems_editor):
    Post = apps.get_model('blog','Post')
    Startup = apps.get_model('organizer','Startups')
    Tag = apps.get_model('organizer','Tag')

    for post_dict in POSTS:
        post = Post.objects.create(
            title=post_dict['title'],
            slug=post_dict['slug'],
            text=post_dict['text'])
        post.pub_date = post_dict['pub_date']
        post.save()
        for tag_slug in post_dict['tags']:
            post.tags.add(
                Tag.objects.get(
                    slug=tag_slug))
        for startup_slug in post_dict['startups']:
            post.startups.add(
                Startup.objects.get(
                    slug=startup_slug))

def remove_post_data(apps, schema_editor):
    Post = apps.get_model('blog','Post')
    for post_dict in POSTS:
        post = Post.objects.get(
            slug=post_dict['slug'])
        post.delete()
    
class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('organizer','0003_startup_data'),
    ]

    operations = [
        migrations.RunPython(
            add_post_data,
            remove_post_data)
    ]

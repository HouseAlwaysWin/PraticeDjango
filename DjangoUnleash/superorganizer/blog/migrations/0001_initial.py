# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=63)),
                ('slug', models.SlugField(help_text='A label for URL config.', unique_for_month='pub_date', max_length=63)),
                ('text', models.TextField()),
                ('pub_date', models.DateField(verbose_name='date published', auto_now_add=True)),
                ('startups', models.ManyToManyField(to='organizer.Startups', related_name='blog_posts')),
                ('tags', models.ManyToManyField(to='organizer.Tag', related_name='blog_posts')),
            ],
            options={
                'get_latest_by': 'pub_date',
                'verbose_name': 'blog_post',
                'ordering': ['-pub_date', 'title'],
            },
        ),
    ]

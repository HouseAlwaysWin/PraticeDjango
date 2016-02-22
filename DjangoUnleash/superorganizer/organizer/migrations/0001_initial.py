# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=63)),
                ('pub_date', models.DateField(verbose_name='date published')),
                ('link', models.URLField(max_length=255)),
            ],
            options={
                'ordering': ['-pub_date'],
                'get_latest_by': 'pub_date',
                'verbose_name': 'news article',
            },
        ),
        migrations.CreateModel(
            name='Startups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(db_index=True, max_length=31)),
                ('slug', models.SlugField(max_length=31, unique=True, help_text='A label for URL config.')),
                ('description', models.TextField()),
                ('founded_date', models.DateField(verbose_name='date founded')),
                ('contact', models.EmailField(max_length=255)),
                ('website', models.URLField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'get_latest_by': 'founded_date',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=31, unique=True)),
                ('slug', models.SlugField(max_length=31, unique=True, help_text='A label for URL config.')),
            ],
        ),
        migrations.AddField(
            model_name='startups',
            name='tags',
            field=models.ManyToManyField(to='organizer.Tag'),
        ),
        migrations.AddField(
            model_name='newslink',
            name='startup',
            field=models.ForeignKey(to='organizer.Startups'),
        ),
    ]

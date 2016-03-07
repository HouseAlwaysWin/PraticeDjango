# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def add_tag_data(apps, schema_editor):
    Tag = apps.get_model('organizer','Tag')
    for tag_name, tag_slug in TAGS:
        Tag.objects.create(
            name=tag_name,
            slug=tag_slug)

def remove_tag_data(apps, schema_editor):
    Tag = apps.get_model('organizer','Tag')
    for _, tag_slug in TAGS:
       tag =  Tag.objects.get(slug=tag_slug)
       tag.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            add_tag_data,
            remove_tag_data)
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

STARTUPS =[
    {
        "name":"Archnobots",
        "slug":"archnobots",
        "contact":"contact@archnobots.com",
        "description":"Remote-controlled internet-enabled",
        "founded_date":date(2014, 10, 31),
        "tags":["mobile","augmented-reality"],
        "website":"http://frightenyourroommate.com/",
    },
]

def add_startup_data(apps, schema_editor):
    Startup = apps.get_model(
        'organizer','Startup')
    Tag = apps.get_model('organizer','Tag')

    for startup in STARTUPS:
        startup_object = Startup.objects.create(
            name=startup['name'],
            slug=startup['slug'],
            contact=startup['contact'],
            description=startup['description'],
            founded_date=startup['founded_date'],
            website=startup['website'])
        
    for tag_slug in startup['tag']:
        startup_object.tags.add(
            Tag.objects.get(
                slug=tag_slug)
            )

def remove_startup_data(apps, shema_editor):
    Startup = apps.get_model(
        'organizer','Startup')
    for startup in STARTUPS:
        startup_object = Startup.object.get(
            slug=startup['slug'])
        startup_object.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0002_tag_data'),
    ]

    operations = [
        migrations.RunPython(
            add_startup_data,
            remove_startup_data)
    ]

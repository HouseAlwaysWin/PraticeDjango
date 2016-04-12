# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.contrib.auth.hashers import make_password


def add_user_data(apps, schema_editor):


def remove_user_data(apps,schema_editor):
    

class Migration(migrations.Migration):

    dependencies = [
        ('blog','0004_post_permissions'),
        ('user', '0002_profile'),
    ]

    operations = [
        migrations.RunPython(
            add_user_data,
            remove_user_data)
    ]

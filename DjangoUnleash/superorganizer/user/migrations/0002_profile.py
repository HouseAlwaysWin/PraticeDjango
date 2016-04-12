# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(max_length=30, unique=True)),
                ('about', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('joined', models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

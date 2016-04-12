# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('slug', models.SlugField(max_length=30, unique=True)),
                ('about', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

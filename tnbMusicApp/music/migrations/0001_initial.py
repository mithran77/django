# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('artist', models.CharField(max_length=250)),
                ('album_title', models.CharField(max_length=500)),
                ('genre', models.CharField(max_length=100)),
                ('album_logo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('file_type', models.CharField(max_length=10)),
                ('song_title', models.CharField(max_length=250)),
                ('album', models.ForeignKey(to='music.Albums')),
            ],
        ),
    ]

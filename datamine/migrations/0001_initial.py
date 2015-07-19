# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataMine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('mine_type', models.CharField(default=b'normal', max_length=50, choices=[(b'normal', b'One Time Scraping'), (b'scheduled', b'Scheduled Scraping')])),
                ('notes', models.TextField(null=True, blank=True)),
                ('status', models.CharField(default=b'pending', max_length=50, choices=[(b'pending', b'Pending'), (b'active', b'Active'), (b'inactive', b'Inactive')])),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DateMineUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='datamine',
            name='sites',
            field=models.ManyToManyField(to='datamine.DateMineUrl', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='datamine',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

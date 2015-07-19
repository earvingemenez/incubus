# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('datamine', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DateMineUrl',
            new_name='DataMineUrl',
        ),
        migrations.AddField(
            model_name='datamine',
            name='data_model',
            field=models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True),
        ),
    ]

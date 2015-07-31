# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_race_position'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='race',
            name='description',
        ),
        migrations.AddField(
            model_name='race',
            name='website',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]

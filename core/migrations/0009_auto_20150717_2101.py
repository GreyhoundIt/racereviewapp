# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_race_gradient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='distance',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'1 Mile'), (1, b'5K'), (2, b'10K'), (3, b'10 Miles'), (4, b'Half Marathon'), (5, b'Marathon'), (6, b'Other')]),
        ),
    ]

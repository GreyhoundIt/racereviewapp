# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150717_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='gradient',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Flat'), (1, b'Slight Hills'), (2, b'Undulating'), (3, b'Hilly')]),
        ),
    ]

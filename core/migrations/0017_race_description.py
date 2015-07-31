# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20150731_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]

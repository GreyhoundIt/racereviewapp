# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150717_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='image_file',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='date',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]

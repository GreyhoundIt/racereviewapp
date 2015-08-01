# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import geoposition.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_race_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 8, 1, 16, 32, 2, 383637, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='race',
            name='position',
            field=geoposition.fields.GeopositionField(max_length=42, null=True, verbose_name=b'Starting Address', blank=True),
        ),
    ]

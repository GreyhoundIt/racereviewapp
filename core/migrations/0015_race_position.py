# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20150718_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='position',
            field=geoposition.fields.GeopositionField(max_length=42, null=True, blank=True),
        ),
    ]

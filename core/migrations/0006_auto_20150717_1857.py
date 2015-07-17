# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20150717_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='description',
            new_name='review',
        ),
    ]

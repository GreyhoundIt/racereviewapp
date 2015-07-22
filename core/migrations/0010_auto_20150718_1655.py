# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20150717_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='changing',
            field=models.CharField(blank=True, max_length=300, null=True, choices=[(b'No', b'No'), (b'Yes', b'Yes')]),
        ),
        migrations.AlterField(
            model_name='race',
            name='medal',
            field=models.CharField(blank=True, max_length=300, null=True, choices=[(b'No', b'No'), (b'Yes', b'Yes')]),
        ),
        migrations.AlterField(
            model_name='race',
            name='scenic',
            field=models.CharField(blank=True, max_length=300, null=True, choices=[(b'No', b'No'), (b'Yes', b'Yes')]),
        ),
        migrations.AlterField(
            model_name='race',
            name='toilets',
            field=models.CharField(blank=True, max_length=300, null=True, choices=[(b'No', b'No'), (b'Yes', b'Yes')]),
        ),
        migrations.AlterField(
            model_name='race',
            name='tshirt',
            field=models.CharField(blank=True, max_length=300, null=True, choices=[(b'No', b'No'), (b'Cotton', b'Cotton'), (b'Technical', b'Technical')]),
        ),
        migrations.AlterField(
            model_name='race',
            name='water',
            field=models.CharField(blank=True, max_length=300, null=True, choices=[(b'No', b'No'), (b'Yes', b'Yes')]),
        ),
    ]

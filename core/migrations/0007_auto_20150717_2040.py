# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20150717_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='changing',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='race',
            name='distance',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'1 Mile'), (1, b'5K'), (2, b'10K'), (3, b'10K'), (4, b'10 Miles'), (5, b'Half Marathon'), (6, b'Marathon'), (7, b'Other')]),
        ),
        migrations.AddField(
            model_name='race',
            name='medal',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='race',
            name='pb',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Yes'), (1, b'Likely'), (2, b'Unlikely'), (3, b'No')]),
        ),
        migrations.AddField(
            model_name='race',
            name='price',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='race',
            name='scenic',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='race',
            name='terrain',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'Road'), (1, b'Trail'), (2, b'Fell'), (3, b'XC'), (4, b'Multiterrain')]),
        ),
        migrations.AddField(
            model_name='race',
            name='toilets',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
        migrations.AddField(
            model_name='race',
            name='tshirt',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Cotton'), (2, b'Technical')]),
        ),
        migrations.AddField(
            model_name='race',
            name='water',
            field=models.IntegerField(blank=True, null=True, choices=[(0, b'No'), (1, b'Yes')]),
        ),
    ]

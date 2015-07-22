# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20150718_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='distance',
            field=models.CharField(blank=True, max_length=300, null=True, choices=[(b'1 Mile', b'1 Mile'), (b'5K', b'5K'), (b'10K', b'10K'), (b'10 Miles', b'10 Miles'), (b'Half Marathon', b'Half Marathon'), (b'Marathon', b'Marathon'), (b'Other', b'Other')]),
        ),
        migrations.AlterField(
            model_name='race',
            name='gradient',
            field=models.CharField(blank=True, max_length=300, null=True, choices=[(b'Flat', b'Flat'), (b'Slight Hills', b'Slight Hills'), (b'Undulating', b'Undulating'), (b'Hilly', b'Hilly')]),
        ),
        migrations.AlterField(
            model_name='race',
            name='pb',
            field=models.CharField(blank=True, max_length=300, null=True, choices=[(b'Yes', b'Yes'), (b'Likely', b'Likely'), (b'Unlikely', b'Unlikely'), (b'No', b'No')]),
        ),
        migrations.AlterField(
            model_name='race',
            name='terrain',
            field=models.CharField(blank=True, max_length=300, null=True, choices=[(b'Road', b'Road'), (b'Trail', b'Trail'), (b'Fell', b'Fell'), (b'XC', b'XC'), (b'Multiterrain', b'Multiterrain')]),
        ),
    ]

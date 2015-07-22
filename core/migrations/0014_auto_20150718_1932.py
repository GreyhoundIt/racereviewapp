# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20150718_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='goodybag',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Goody Bag', choices=[(0, b'None'), (1, b'*'), (2, b'**'), (3, b'***'), (4, b'****'), (5, b'*****')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Overall Raiting', choices=[(0, b'None'), (1, b'*'), (2, b'**'), (3, b'***'), (4, b'****'), (5, b'*****')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='valueformoney',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'Value for money', choices=[(0, b'None'), (1, b'*'), (2, b'**'), (3, b'***'), (4, b'****'), (5, b'*****')]),
        ),
    ]

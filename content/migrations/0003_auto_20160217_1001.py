# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20160217_0802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourstory',
            name='order',
            field=models.CharField(default=1, max_length=7, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]),
        ),
    ]

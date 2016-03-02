# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_ourstorytitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourstory',
            name='color',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20160217_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourstory',
            name='order',
            field=models.PositiveIntegerField(),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_auto_20160302_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourteam',
            name='img',
            field=models.ImageField(null=True, blank=True, upload_to=''),
        ),
    ]

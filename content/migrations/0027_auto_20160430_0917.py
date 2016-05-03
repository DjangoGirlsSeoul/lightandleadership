# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0026_auto_20160428_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footerinfo',
            name='learnmorelink',
            field=models.CharField(default='#', max_length=200),
        ),
    ]

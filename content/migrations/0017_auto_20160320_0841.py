# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0016_auto_20160320_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourstory',
            name='order',
            field=models.CharField(help_text='Enter a number. 1 will be at the top of the page', max_length=2),
        ),
    ]

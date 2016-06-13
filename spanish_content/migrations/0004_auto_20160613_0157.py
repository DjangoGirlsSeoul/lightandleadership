# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spanish_content', '0003_auto_20160613_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submenu',
            name='order',
            field=models.PositiveIntegerField(help_text='Enter a number 1 will be on the top of a dropdown'),
        ),
    ]

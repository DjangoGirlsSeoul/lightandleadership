# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0036_auto_20160613_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='order',
            field=models.PositiveIntegerField(help_text='Enter a number. 1 will be on the left.'),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='order',
            field=models.PositiveIntegerField(help_text='Enter a number. 1 will be on the top of a dropdown.'),
        ),
    ]

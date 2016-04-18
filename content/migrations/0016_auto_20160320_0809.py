# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eduprogram',
            name='color',
            field=models.CharField(help_text="Only enter a color if the order >= 2. Both 'red' and '#FF0000' are accceptable", max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='eduprogram',
            name='order',
            field=models.PositiveIntegerField(help_text='Enter a number. 1 will be at the top of the page'),
        ),
        migrations.AlterField(
            model_name='eduprogram',
            name='text',
            field=models.TextField(null=True, help_text='Enter a short description of program.', blank=True),
        ),
    ]

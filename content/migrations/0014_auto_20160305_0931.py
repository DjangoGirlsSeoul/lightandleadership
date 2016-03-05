# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_auto_20160305_0915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eduprogram',
            old_name='postcategory',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='eduprogram',
            name='color',
            field=models.CharField(help_text="Both 'red' and '#FF0000' are accceptable", max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='eduprogram',
            name='img',
            field=models.ImageField(help_text='Only upload an image if order = 1', upload_to='education', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='eduprogram',
            name='order',
            field=models.PositiveIntegerField(help_text='1 will be the top of the page'),
        ),
    ]

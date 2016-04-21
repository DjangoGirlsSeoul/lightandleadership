# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0020_auto_20160418_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerabout',
            name='text',
            field=tinymce.models.HTMLField(null=True, help_text='For order number 2+: Enter a short description.', blank=True),
        ),
        migrations.AlterField(
            model_name='volunteerabout',
            name='title',
            field=models.CharField(null=True, help_text='If the order number is 1, this will be the page title.', blank=True, max_length=100),
        ),
    ]

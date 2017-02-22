# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0038_auto_20161013_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='button_text',
            field=models.CharField(null=True, max_length=100, blank=True, default='Learn More'),
        ),
    ]

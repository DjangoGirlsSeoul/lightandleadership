# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('spanish_content', '0006_auto_20161013_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='button_text',
            field=models.CharField(blank=True, default='Learn More', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='board_team',
            field=tinymce.models.HTMLField(help_text='Enter a short description', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='peru_team',
            field=tinymce.models.HTMLField(help_text='Enter a short description', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='us_team',
            field=tinymce.models.HTMLField(help_text='Enter a short description', null=True, blank=True),
        ),
    ]

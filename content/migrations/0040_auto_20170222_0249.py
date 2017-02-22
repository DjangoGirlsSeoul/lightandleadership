# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0039_home_button_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='footerinfo',
            name='copyright',
            field=models.CharField(default=' ', max_length=300),
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

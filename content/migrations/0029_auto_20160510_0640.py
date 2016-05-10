# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0028_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourteam',
            name='title',
            field=models.CharField(default='header', max_length=200),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='board_team',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='img',
            field=models.ImageField(help_text='This will be the page title image.', null=True, upload_to='aboutus', blank=True),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='peru_team',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='us_team',
            field=models.CharField(max_length=300),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0023_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('img', models.ImageField(blank=True, help_text='Upload image for footer', null=True, upload_to='volunteer')),
                ('title', models.CharField(max_length=100, blank=True, help_text='Enter Footer Title', null=True)),
                ('text', tinymce.models.HTMLField(blank=True, help_text='Enter a short description.', null=True)),
                ('learnmorelink', models.URLField(default='#')),
                ('facebooklink', models.URLField(default='#')),
                ('twitterlink', models.URLField(default='#')),
                ('instagramlink', models.URLField(default='#')),
            ],
        ),
        migrations.AlterField(
            model_name='eduprogram',
            name='text',
            field=tinymce.models.HTMLField(blank=True, help_text='Enter a short description of program.', null=True),
        ),
    ]

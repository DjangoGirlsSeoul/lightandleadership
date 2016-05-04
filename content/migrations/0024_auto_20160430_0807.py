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
            name='Home',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('img', models.ImageField(blank=True, upload_to='aboutus', null=True)),
                ('text', tinymce.models.HTMLField(default='')),
                ('color', models.CharField(blank=True, max_length=20)),
                ('order', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='eduprogram',
            name='text',
            field=tinymce.models.HTMLField(blank=True, help_text='Enter a short description of program.', null=True),
        ),
    ]

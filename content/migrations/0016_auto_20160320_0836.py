# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eduprogram',
            name='color',
            field=models.CharField(max_length=20, blank=True, help_text="Only enter a color if the order >= 2. Both 'red' and '#FF0000' are accceptable"),
        ),
        migrations.AlterField(
            model_name='eduprogram',
            name='order',
            field=models.PositiveIntegerField(help_text='Enter a number. 1 will be at the top of the page'),
        ),
        migrations.AlterField(
            model_name='eduprogram',
            name='text',
            field=tinymce.models.HTMLField(null=True, blank=True, help_text='Enter a short description of program.'),
        ),
        migrations.AlterField(
            model_name='ourstory',
            name='color',
            field=models.CharField(max_length=20, blank=True, help_text="Only enter a color if the order >= 2. Both 'red' and '#FF0000' are accceptable"),
        ),
        migrations.AlterField(
            model_name='ourstory',
            name='img',
            field=models.ImageField(upload_to='aboutus', null=True, blank=True, help_text='Only upload an image if order = 1'),
        ),
        migrations.AlterField(
            model_name='ourstory',
            name='order',
            field=models.PositiveIntegerField(help_text='Enter a number. 1 will be at the top of the page'),
        ),
        migrations.AlterField(
            model_name='ourstory',
            name='text',
            field=tinymce.models.HTMLField(null=True, blank=True, help_text='Enter a short description of program.'),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='text',
            field=tinymce.models.HTMLField(),
        ),
    ]

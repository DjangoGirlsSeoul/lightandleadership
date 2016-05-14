# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0028_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonateInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('order', models.PositiveIntegerField(help_text='Enter a number. 1 will be at the top of the page')),
                ('color', models.CharField(blank=True, help_text='Only enter a color if the order is 1 ', max_length=20)),
                ('title', models.CharField(blank=True, help_text='If the order number is 1, this will be the section title.', null=True, max_length=100)),
                ('img', models.ImageField(blank=True, help_text='Upload image corresponding to Text', null=True, upload_to='action')),
                ('text', tinymce.models.HTMLField(blank=True, help_text='Enter a short description', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='board_team',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='img',
            field=models.ImageField(blank=True, help_text='This will be the page title image.', null=True, upload_to='aboutus'),
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

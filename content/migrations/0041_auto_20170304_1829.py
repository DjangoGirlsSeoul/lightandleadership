# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0040_auto_20170222_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='button_text2',
            field=models.CharField(blank=True, default='Learn More', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='link2',
            field=models.URLField(blank=True, default='#', help_text='Please enter a link for learn more button', null=True),
        ),
    ]
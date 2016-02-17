# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourstory',
            name='order',
            field=models.CharField(max_length=7, default='first', choices=[('first', 'first'), ('second', 'second'), ('third', 'third')]),
        ),
        migrations.AlterField(
            model_name='ourstory',
            name='color',
            field=models.CharField(max_length=6, blank=True),
        ),
        migrations.AlterField(
            model_name='ourstory',
            name='img',
            field=models.ImageField(upload_to='', blank=True, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_auto_20160302_1020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childrensprogram',
            name='title',
        ),
        migrations.AddField(
            model_name='childrensprogram',
            name='pagetitle',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='childrensprogram',
            name='subtitle',
            field=models.CharField(blank=True, null=True, max_length=50),
        ),
    ]

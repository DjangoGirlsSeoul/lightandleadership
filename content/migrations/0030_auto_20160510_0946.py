# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0029_auto_20160510_0824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donateinfo',
            name='color',
        ),
        migrations.AlterField(
            model_name='volunteerperu',
            name='category',
            field=models.CharField(choices=[('Donate', 'Donate'), ('Club', 'Club'), ('Paypal', 'Paypal')], max_length=15, default='Donate'),
        ),
    ]

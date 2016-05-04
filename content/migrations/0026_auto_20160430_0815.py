# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0025_home_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='color',
            field=models.CharField(blank=True, max_length=20, help_text="Only enter a color if the order >= 2. Both 'red' and '#FF0000' are accceptable"),
        ),
    ]

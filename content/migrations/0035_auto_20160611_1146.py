# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0034_menu_menunavbar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='parent_category',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]

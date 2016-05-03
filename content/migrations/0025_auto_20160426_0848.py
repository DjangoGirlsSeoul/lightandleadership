# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0024_auto_20160426_0830'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomPage',
            new_name='CustomPage1',
        ),
    ]

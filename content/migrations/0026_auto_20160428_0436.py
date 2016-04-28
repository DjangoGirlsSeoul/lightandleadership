# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0025_auto_20160426_0848'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomPage1',
            new_name='CustomPage',
        ),
    ]

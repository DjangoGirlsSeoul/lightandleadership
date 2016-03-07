# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_auto_20160305_0907'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EduProgram',
            new_name='EduPrograms',
        ),
    ]

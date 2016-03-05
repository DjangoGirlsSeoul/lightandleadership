# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_auto_20160305_0913'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EduPrograms',
            new_name='EduProgram',
        ),
    ]

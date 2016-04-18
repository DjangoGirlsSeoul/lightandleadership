# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0019_auto_20160418_1344'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CurrentNeeds',
            new_name='VolunteerOpenPosition',
        ),
    ]

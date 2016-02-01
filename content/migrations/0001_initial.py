# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ourstory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('img', models.ImageField(upload_to='/uploads')),
                ('text', models.TextField()),
                ('color', models.CharField(max_length=6)),
            ],
        ),
    ]

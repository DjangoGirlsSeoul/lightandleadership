# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ourteam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to='uploads')),
                ('text', models.TextField()),
                ('us_team', models.CharField(max_length=100)),
                ('peru_team', models.CharField(max_length=100)),
                ('board_team', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='ourstory',
            name='img',
            field=models.ImageField(upload_to='uploads'),
        ),
    ]

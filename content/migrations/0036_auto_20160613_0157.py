# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0035_auto_20160611_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(help_text='Enter a number 1 will be on the left')),
                ('title', models.CharField(null=True, max_length=100)),
                ('link', models.CharField(blank=True, null=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(help_text='Enter a number 1 will be on the top of a dropdown')),
                ('title', models.CharField(null=True, max_length=100)),
                ('link', models.CharField(blank=True, null=True, max_length=100)),
                ('menu', models.ForeignKey(to='content.Menu')),
            ],
        ),
        migrations.RemoveField(
            model_name='menunavbar',
            name='parent',
        ),
        migrations.DeleteModel(
            name='MenuNavbar',
        ),
    ]

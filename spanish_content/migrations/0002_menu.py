# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spanish_content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('order', models.PositiveIntegerField(help_text='Enter a number 1 will be on the left')),
                ('title', models.CharField(max_length=100, null=True, blank=True)),
                ('parent', models.ForeignKey(related_name='child', null=True, blank=True, to='spanish_content.Menu')),
            ],
        ),
    ]

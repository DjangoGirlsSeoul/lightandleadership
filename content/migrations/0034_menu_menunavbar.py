# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0033_auto_20160521_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(help_text='write menu title', max_length=20)),
                ('order', models.PositiveIntegerField(help_text='enter a number 1 will be on the left')),
                ('parent_category', models.ForeignKey(blank=True, to='content.Menu', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuNavbar',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('link', models.CharField(max_length=100, verbose_name='link')),
                ('title', models.CharField(max_length=250, verbose_name='title')),
                ('parent', models.ForeignKey(blank=True, to='content.MenuNavbar', null=True, related_name='child')),
            ],
            options={
                'verbose_name_plural': 'MenuNavbars',
                'ordering': ['title'],
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spanish_content', '0002_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('order', models.PositiveIntegerField(help_text='Enter a number 1 will be on the left')),
                ('title', models.CharField(max_length=100, null=True)),
                ('link', models.CharField(blank=True, null=True, max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='menu',
            name='parent',
        ),
        migrations.AddField(
            model_name='menu',
            name='link',
            field=models.CharField(blank=True, null=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='submenu',
            name='menu',
            field=models.ForeignKey(to='spanish_content.Menu'),
        ),
    ]

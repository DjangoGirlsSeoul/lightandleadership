# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildrensProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('subtitle', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('color', models.CharField(max_length=20, blank=True)),
                ('order', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='ourstory',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

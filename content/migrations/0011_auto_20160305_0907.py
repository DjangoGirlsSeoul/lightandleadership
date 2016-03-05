# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_auto_20160302_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='EduProgram',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(null=True, blank=True, max_length=100)),
                ('img', models.ImageField(null=True, blank=True, upload_to='education')),
                ('text', models.TextField(null=True, blank=True)),
                ('color', models.CharField(blank=True, max_length=20)),
                ('order', models.PositiveIntegerField()),
                ('postcategory', models.CharField(choices=[('Children', 'Children'), ('Teens', 'Teens'), ('Women', 'Women'), ('Artisan', 'Artisan')], default='Children', max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='ChildrensProgram',
        ),
        migrations.AlterField(
            model_name='ourstory',
            name='img',
            field=models.ImageField(null=True, blank=True, upload_to='aboutus'),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='img',
            field=models.ImageField(null=True, blank=True, upload_to='aboutus'),
        ),
    ]

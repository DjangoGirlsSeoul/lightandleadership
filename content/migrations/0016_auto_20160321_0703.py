# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='EthicalPost',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, help_text='Only enter a title if order is 1. This is the page title.', blank=True, null=True)),
                ('img', models.ImageField(upload_to='aboutus', help_text='Upload image corresponding to Text', blank=True, null=True)),
                ('text', models.TextField(help_text='Enter a short description.', blank=True, null=True)),
                ('order', models.CharField(max_length=2, help_text='Enter a number. 1 will be at the top of the page')),
            ],
        ),
        migrations.AlterField(
            model_name='eduprogram',
            name='color',
            field=models.CharField(help_text="Only enter a color if the order >= 2. Both 'red' and '#FF0000' are accceptable", blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='eduprogram',
            name='order',
            field=models.PositiveIntegerField(help_text='Enter a number. 1 will be at the top of the page'),
        ),
        migrations.AlterField(
            model_name='eduprogram',
            name='text',
            field=models.TextField(help_text='Enter a short description of program.', blank=True, null=True),
        ),
    ]

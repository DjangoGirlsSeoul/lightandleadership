# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0030_auto_20160510_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonateSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(help_text='Enter a number. 1 will be at the top of the page')),
                ('color', models.CharField(help_text='Only enter a color if the order is 1 ', blank=True, max_length=20)),
                ('title', models.CharField(null=True, blank=True, help_text='If the order number is 1, this will be the section title.', max_length=100)),
                ('img', models.ImageField(null=True, upload_to='action', blank=True, help_text='Upload image corresponding to Text')),
                ('text', tinymce.models.HTMLField(null=True, help_text='Enter a short description', blank=True)),
                ('category', models.CharField(default='Donate', choices=[('Donate', 'Donate'), ('Club', 'Club'), ('Paypal', 'Paypal')], max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='volunteerperu',
            name='category',
            field=models.CharField(default='Volunteers', choices=[('Volunteers', 'Volunteers'), ('Intership', 'Intership'), ('Fees', 'Fees')], max_length=15),
        ),
    ]

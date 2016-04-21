# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0021_auto_20160421_0641'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('Chicago', 'Chicago'), ('Donations', 'Donations'), ('Financials', 'Financials'), ('WhyPeru', 'WhyPeru')], default='Chicago', max_length=15)),
                ('order', models.PositiveIntegerField(help_text='Enter a number. 1 will be at the top of the page')),
                ('title', models.CharField(blank=True, help_text='If the order number is 1, this will be the page title.', null=True, max_length=100)),
                ('img', models.ImageField(blank=True, help_text='Upload image corresponding to Text', null=True, upload_to='volunteer')),
                ('text', tinymce.models.HTMLField(blank=True, help_text='Enter a short description.', null=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0032_merge'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DonateInfo',
        ),
        migrations.AlterField(
            model_name='donatesection',
            name='category',
            field=models.CharField(choices=[('AboutUs', 'AboutUs'), ('Donate', 'Donate'), ('Club', 'Club'), ('Paypal', 'Paypal')], default='Donate', max_length=15),
        ),
        migrations.AlterField(
            model_name='donatesection',
            name='color',
            field=models.CharField(help_text='This is the background color for section titles, Only needed if order = 1.', max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='donatesection',
            name='order',
            field=models.PositiveIntegerField(help_text='Enter a number. 1 will be at the top'),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='title',
            field=models.CharField(default='Our Team', max_length=200),
        ),
    ]

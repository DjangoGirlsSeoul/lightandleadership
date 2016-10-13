# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spanish_content', '0005_auto_20160614_0749'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeLink',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('link', models.URLField(help_text='Please enter a link')),
                ('title', models.CharField(blank=True, null=True, max_length=100)),
                ('color', models.CharField(blank=True, max_length=20, help_text="Only enter a color if the order >= 2. Both 'red' and '#FF0000' are accceptable")),
                ('order', models.PositiveIntegerField(default=1)),
                ('icon', models.CharField(blank=True, null=True, max_length=100, default='fa-heart', help_text="Please write in which icon you'd like, ie fa-phone. Check <a href='http://fontawesome.io/icons/'>here</a> for icons.")),
            ],
        ),
        migrations.AddField(
            model_name='home',
            name='link',
            field=models.URLField(default='#', help_text='Please enter a link for learn more button'),
        ),
    ]

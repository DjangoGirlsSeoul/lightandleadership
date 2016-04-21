# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0018_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentNeeds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(help_text='Please enter the position title', max_length=100, blank=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, help_text='Please enter the start date for the position')),
                ('link', models.URLField(help_text='Please enter a link for the application')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerAbout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('order', models.PositiveIntegerField(help_text='Enter a number. 1 will be at the top of the page')),
                ('title', models.CharField(null=True, help_text='Only necessary for order number 1: Enter the page title', max_length=20, blank=True)),
                ('text', tinymce.models.HTMLField(null=True, blank=True, help_text='For order number 2: Enter a short description.')),
                ('img', models.ImageField(upload_to='action', null=True, help_text='Upload image corresponding to Text', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerPeru',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('order', models.PositiveIntegerField(help_text='Enter a number. 1 will be at the top of the page')),
                ('color', models.CharField(help_text='Only enter a color if the order is 1 ', max_length=20, blank=True)),
                ('title', models.CharField(null=True, help_text='If the order number is 1, this will be the section title.', max_length=100, blank=True)),
                ('img', models.ImageField(upload_to='action', null=True, help_text='Upload image corresponding to Text', blank=True)),
                ('text', tinymce.models.HTMLField(null=True, blank=True, help_text='Enter a short description')),
                ('category', models.CharField(default='Volunteers', choices=[('Volunteers', 'Volunteers'), ('Intership', 'Intership'), ('Fees', 'Fees')], max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='eduprogram',
            name='text',
            field=tinymce.models.HTMLField(null=True, blank=True, help_text='Enter a short description of program.'),
        ),
        migrations.AlterField(
            model_name='ethicalpost',
            name='order',
            field=models.PositiveIntegerField(help_text='Enter a number. 1 will be at the top of the page'),
        ),
        migrations.AlterField(
            model_name='ethicalpost',
            name='text',
            field=tinymce.models.HTMLField(null=True, blank=True, help_text='Enter a short description.'),
        ),
        migrations.AlterField(
            model_name='ethicalpost',
            name='title',
            field=models.CharField(null=True, help_text='If the order number is 1, this will be the page title.', max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='ourstory',
            name='color',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='ourstory',
            name='img',
            field=models.ImageField(upload_to='aboutus', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ourstory',
            name='order',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='ourstory',
            name='text',
            field=tinymce.models.HTMLField(default=''),
        ),
    ]

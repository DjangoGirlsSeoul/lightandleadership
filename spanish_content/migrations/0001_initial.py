# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomPage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('category', models.CharField(choices=[('Chicago', 'Chicago'), ('Donations', 'Donations'), ('Financials', 'Financials'), ('WhyPeru', 'WhyPeru')], default='Chicago', max_length=15)),
                ('order', models.PositiveIntegerField(help_text='Enter a number. 1 will be at the top of the page')),
                ('title', models.CharField(blank=True, max_length=100, null=True, help_text='If the order number is 1, this will be the page title.')),
                ('img', models.ImageField(blank=True, upload_to='volunteer', null=True, help_text='Upload image corresponding to Text')),
                ('text', tinymce.models.HTMLField(blank=True, null=True, help_text='Enter a short description.')),
            ],
        ),
        migrations.CreateModel(
            name='DonateSection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('order', models.PositiveIntegerField(help_text='Enter a number. 1 will be at the top')),
                ('color', models.CharField(max_length=20, blank=True, help_text='This is the background color for section titles, Only needed if order = 1.')),
                ('title', models.CharField(blank=True, max_length=100, null=True, help_text='If the order number is 1, this will be the section title.')),
                ('img', models.ImageField(blank=True, upload_to='action', null=True, help_text='Upload image corresponding to Text')),
                ('text', tinymce.models.HTMLField(blank=True, null=True, help_text='Enter a short description')),
                ('category', models.CharField(choices=[('AboutUs', 'AboutUs'), ('Donate', 'Donate'), ('Club', 'Club'), ('Paypal', 'Paypal')], default='Donate', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='EduProgram',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=100, blank=True, null=True)),
                ('img', models.ImageField(blank=True, upload_to='education', null=True, help_text='Only upload an image if order = 1')),
                ('text', tinymce.models.HTMLField(blank=True, null=True, help_text='Enter a short description of program.')),
                ('color', models.CharField(max_length=20, blank=True, help_text="Only enter a color if the order >= 2. Both 'red' and '#FF0000' are accceptable")),
                ('order', models.PositiveIntegerField(help_text='Enter a number. 1 will be at the top of the page')),
                ('category', models.CharField(choices=[('Children', 'Children'), ('Teens', 'Teens'), ('Women', 'Women'), ('Artisan', 'Artisan')], default='Children', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='EthicalPost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True, help_text='If the order number is 1, this will be the page title.')),
                ('img', models.ImageField(blank=True, upload_to='aboutus', null=True, help_text='Upload image corresponding to Text')),
                ('text', tinymce.models.HTMLField(blank=True, null=True, help_text='Enter a short description.')),
                ('order', models.PositiveIntegerField(help_text='Enter a number. 1 will be at the top of the page')),
            ],
        ),
        migrations.CreateModel(
            name='FooterInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('img', models.ImageField(blank=True, upload_to='volunteer', null=True, help_text='Upload image for footer')),
                ('title', models.CharField(blank=True, max_length=100, null=True, help_text='Enter Footer Title')),
                ('text', tinymce.models.HTMLField(blank=True, null=True, help_text='Enter a short description.')),
                ('learnmorelink', models.CharField(default='#', max_length=200)),
                ('facebooklink', models.URLField(default='#')),
                ('twitterlink', models.URLField(default='#')),
                ('instagramlink', models.URLField(default='#')),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=100, blank=True, null=True)),
                ('color', models.CharField(max_length=20, blank=True, help_text="Only enter a color if the order >= 2. Both 'red' and '#FF0000' are accceptable")),
                ('order', models.PositiveIntegerField()),
                ('img', models.ImageField(upload_to='aboutus', blank=True, null=True)),
                ('text', tinymce.models.HTMLField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='OurStory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('img', models.ImageField(upload_to='aboutus', blank=True, null=True)),
                ('text', tinymce.models.HTMLField(default='')),
                ('color', models.CharField(max_length=20, blank=True)),
                ('order', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OurStoryTitle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(default='Our Team', max_length=200)),
                ('img', models.ImageField(blank=True, upload_to='aboutus', null=True, help_text='This will be the page title image.')),
                ('text', tinymce.models.HTMLField()),
                ('us_team', models.CharField(max_length=300)),
                ('peru_team', models.CharField(max_length=300)),
                ('board_team', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerAbout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('order', models.PositiveIntegerField(help_text='Enter a number. 1 will be at the top of the page')),
                ('title', models.CharField(blank=True, max_length=100, null=True, help_text='If the order number is 1, this will be the page title.')),
                ('text', tinymce.models.HTMLField(blank=True, null=True, help_text='For order number 2+: Enter a short description.')),
                ('img', models.ImageField(blank=True, upload_to='action', null=True, help_text='Upload image corresponding to Text')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerOpenPosition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=100, blank=True, help_text='Please enter the position title')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, help_text='Please enter the start date for the position')),
                ('link', models.URLField(help_text='Please enter a link for the application')),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerPeru',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('order', models.PositiveIntegerField(help_text='Enter a number. 1 will be at the top of the page')),
                ('color', models.CharField(max_length=20, blank=True, help_text='Only enter a color if the order is 1 ')),
                ('title', models.CharField(blank=True, max_length=100, null=True, help_text='If the order number is 1, this will be the section title.')),
                ('img', models.ImageField(blank=True, upload_to='action', null=True, help_text='Upload image corresponding to Text')),
                ('text', tinymce.models.HTMLField(blank=True, null=True, help_text='Enter a short description')),
                ('category', models.CharField(choices=[('Volunteers', 'Volunteers'), ('Intership', 'Intership'), ('Fees', 'Fees')], default='Volunteers', max_length=15)),
            ],
        ),
    ]

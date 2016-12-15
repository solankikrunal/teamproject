# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-15 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_type', models.CharField(max_length=120)),
                ('rooms', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.IntegerField(default=0)),
                ('images', models.FileField(null=True, upload_to=b'')),
                ('details', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='SignUP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=60)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='profile_picture',
            field=models.ImageField(upload_to='team/'),
        ),
    ]

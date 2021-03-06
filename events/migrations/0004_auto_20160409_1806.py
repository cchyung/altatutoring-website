# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-10 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20160331_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(help_text='Description.', max_length=500),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(help_text='Location of event.', max_length=500),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(help_text='Name of the event.', max_length=250),
        ),
    ]

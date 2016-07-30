# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0006_auto_20160331_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='title',
            field=models.CharField(default='Team Member', help_text='ie. CEO or Self-Proclaimed Smartest Man Alive.', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='bio',
            field=models.TextField(help_text='Include a short bio about yourself and any other information you need. ie. John Smith likes to go fishing on the weekends.', max_length=500),
        ),
        migrations.AlterField(
            model_name='member',
            name='profile_picture',
            field=models.ImageField(help_text='This picture needs to have square dimensions or it will render incorrectly.', upload_to='team/'),
        ),
    ]

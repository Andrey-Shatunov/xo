# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-04 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xo', '0004_steps_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='user_one',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='room',
            name='user_two',
            field=models.CharField(default='', max_length=200),
        ),
    ]

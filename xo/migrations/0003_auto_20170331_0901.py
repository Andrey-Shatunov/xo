# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-31 04:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xo', '0002_statistics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(default='', max_length=200)),
                ('user_one', models.IntegerField(default=0)),
                ('user_two', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='steps',
            name='room',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='xo.Room'),
        ),
    ]
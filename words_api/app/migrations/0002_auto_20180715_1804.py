# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-15 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='anagramCount',
        ),
        migrations.RemoveField(
            model_name='word',
            name='id',
        ),
        migrations.AddField(
            model_name='word',
            name='length',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='word',
            name='letters',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='word',
            name='word',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-23 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190123_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='dochod',
            field=models.ManyToManyField(to='app.Dochod'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-23 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190123_1400'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dochod',
            options={'ordering': ['-description', '-pk']},
        ),
        migrations.AddField(
            model_name='dochod',
            name='dochod_id',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='dochod',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
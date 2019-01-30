# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-30 10:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_wallet_dochod'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wydatek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wydatek_id', models.BigIntegerField(default=0)),
                ('description', models.CharField(max_length=1000)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=18)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='WydatekCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='wydatek',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.WydatekCategory'),
        ),
        migrations.AddField(
            model_name='wallet',
            name='wydatek',
            field=models.ManyToManyField(to='app.Wydatek'),
        ),
    ]
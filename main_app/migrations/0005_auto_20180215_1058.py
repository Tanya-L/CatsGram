# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-15 10:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20180214_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='litter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Litter'),
        ),
    ]

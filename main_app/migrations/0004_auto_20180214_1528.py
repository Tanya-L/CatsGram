# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-14 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20180214_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Litter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('breeder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Breeder')),
            ],
        ),
        migrations.RemoveField(
            model_name='cat',
            name='breeder',
        ),
        migrations.AddField(
            model_name='litter',
            name='father',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='father_litter', to='main_app.Cat'),
        ),
        migrations.AddField(
            model_name='litter',
            name='mother',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mother_litter', to='main_app.Cat'),
        ),
        migrations.AddField(
            model_name='cat',
            name='litter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Litter'),
        ),
    ]

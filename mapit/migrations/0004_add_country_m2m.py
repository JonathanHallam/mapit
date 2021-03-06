# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-22 17:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapit', '0003_auto_20161205_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='countries',
            field=models.ManyToManyField(blank=True, related_name='areas_m2m', to='mapit.Country'),
        ),
        migrations.AlterField(
            model_name='area',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='areas_direct', to='mapit.Country'),
        ),
    ]

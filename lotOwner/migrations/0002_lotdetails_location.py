# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-16 16:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lotOwner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lotdetails',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lotOwner.Location'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-11 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180609_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverprofile',
            name='license',
            field=models.IntegerField(null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-10 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotOwner', '0002_auto_20180610_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='lotdetails',
            name='Image_of_Lot',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
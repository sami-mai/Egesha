# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-20 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180617_1723'),
        ('lotOwner', '0005_auto_20180617_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bank_name', models.CharField(max_length=40)),
                ('Account_number', models.CharField(max_length=40)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.OwnerProfile')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-22 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paymode',
            field=models.CharField(blank=True, choices=[('0', 'Cash On Deilvery'), ('1', 'Paid')], max_length=1, null=True, verbose_name='Payment Mode'),
        ),
    ]

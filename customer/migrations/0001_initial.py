# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 16:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('train', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='Mobile Number')),
                ('wallet_amount', models.IntegerField(blank=True, default=0, verbose_name='Wallet Amount')),
                ('time_stamp', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('0', 'Pending'), ('1', 'Received'), ('2', 'Preparing'), ('3', 'Prepared'), ('4', 'Dispatched'), ('5', 'Delivered'), ('8', 'Cancelled'), ('9', 'Cancelled by Vendor')], max_length=1, null=True, verbose_name='Status of Order')),
                ('time_stamp', models.DateTimeField(auto_now=True, null=True)),
                ('cust', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Fooditem')),
                ('pnr_no', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='train.Pnr')),
                ('shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Shop')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Message')),
                ('time_stamp', models.DateTimeField(auto_now=True, null=True)),
                ('cust', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
                ('shop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Shop')),
            ],
            options={
                'db_table': 'review',
            },
        ),
    ]

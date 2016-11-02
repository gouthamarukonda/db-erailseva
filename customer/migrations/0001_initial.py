# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 22:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('train', '0001_initial'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
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
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='Quantity')),
                ('status', models.CharField(blank=True, choices=[('0', 'Pending'), ('1', 'Received'), ('2', 'Preparing'), ('3', 'Prepared'), ('4', 'Dispatched'), ('5', 'Delivered'), ('8', 'Cancelled'), ('9', 'Cancelled by Vendor')], default='0', max_length=1, verbose_name='Status of Order')),
                ('time_stamp', models.DateTimeField(auto_now=True, null=True)),
                ('cust', models.ForeignKey(blank=True, db_column='cust_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
                ('item', models.ForeignKey(blank=True, db_column='item_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Fooditem')),
                ('pnr', models.ForeignKey(blank=True, db_column='pnr_no', null=True, on_delete=django.db.models.deletion.CASCADE, to='train.Pnr')),
                ('shop', models.ForeignKey(blank=True, db_column='shop_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Shop')),
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
                ('cust', models.ForeignKey(blank=True, db_column='cust_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
                ('shop', models.ForeignKey(blank=True, db_column='shop_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Shop')),
            ],
            options={
                'db_table': 'review',
            },
        ),
    ]

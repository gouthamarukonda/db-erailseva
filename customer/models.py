from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from train.models import Pnr
from shop.models import Shop, Fooditem

# Create your models here.

class Customer(models.Model):

	cust_id = models.CharField("Customer Id", max_length = 10, primary_key = True)
	user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
	# User: username, password, first_name, last_name, email
	mobile = models.CharField("Mobile Number", max_length = 11, null = True, blank = True)
	wallet_amount = models.IntegerField("Wallet Amount", null = True, blank = True)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)

	class Meta:
		db_table = 'customers'

class Order(models.Model):

	STATUS_PENDING = '0'
	STATUS_RECEIVED = '1'
	STATUS_PREPARING = '2'
	STATUS_PREPARED = '3'
	STATUS_DISPATCHED = '4'
	STATUS_DELIVERED = '5'
	STATUS_CANCELLED = '8'
	STATUS_CANCELLED_BY_VENDOR = '9'

	STATUS_CHOICES = (
		(STATUS_PENDING, 'Pending'),
		(STATUS_RECEIVED, 'Received'),
		(STATUS_PREPARING, 'Preparing'),
		(STATUS_PREPARED, 'Prepared'),
		(STATUS_DISPATCHED, 'Dispatched'),
		(STATUS_DELIVERED, 'Delivered'),
		(STATUS_CANCELLED, 'Cancelled'),
		(STATUS_CANCELLED_BY_VENDOR, 'Cancelled by Vendor'),
	)

	pnr_no = models.ForeignKey(Pnr, blank = True, null = True, on_delete = models.CASCADE)
	cust_id = models.ForeignKey(Customer, blank = True, null = True, on_delete = models.CASCADE)
	shop_id = models.ForeignKey(Shop, blank = True, null = True, on_delete = models.CASCADE)
	item_id = models.ForeignKey(Fooditem, blank = True, null = True, on_delete = models.CASCADE)
	status = models.CharField("Status of Order", choices = STATUS_CHOICES, max_length = 1, blank = True, null = True)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)

	class Meta:
		db_table = 'orders'

class Review(models.Model):

	cust_id = models.ForeignKey(Customer, blank = True, null = True, on_delete = models.CASCADE)
	shop_id = models.ForeignKey(Shop, blank = True, null = True, on_delete = models.CASCADE)
	msg = models.CharField("Message", max_length = 1000, blank = True, null = True)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)

	class Meta:
		db_table = 'reviews'

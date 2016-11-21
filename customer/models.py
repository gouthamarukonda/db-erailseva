from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from train.models import Pnr
from shop.models import Shop, Fooditem

# Create your models here.

class Customer(models.Model):

	user = models.OneToOneField(User, primary_key = True, db_column = 'user_id', on_delete = models.CASCADE)
	# User: *username, *password, first_name, last_name, *email
	mobile = models.CharField("Mobile Number", max_length = 11, null = True, blank = True)
	wallet_amount = models.IntegerField("Wallet Amount", blank = True, default = 0)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)

	class Meta:
		db_table = 'customer'

	def __unicode__(self):
		return unicode(self.user)

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

	order_id = models.AutoField(primary_key = True)
	pnr = models.ForeignKey(Pnr, blank = True, null = True, db_column = 'pnr_no', on_delete = models.CASCADE)
	cust = models.ForeignKey(Customer, blank = True, null = True, db_column = 'cust_id', on_delete = models.CASCADE)
	shop = models.ForeignKey(Shop, blank = True, null = True, db_column = 'shop_id', on_delete = models.CASCADE)
	item = models.ForeignKey(Fooditem, blank = True, null = True, db_column = 'item_id', on_delete = models.CASCADE)
	quantity = models.IntegerField("Quantity", blank = True, null = True)
	status = models.CharField("Status of Order", choices = STATUS_CHOICES, max_length = 1, blank = True, default = STATUS_PENDING)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)

	class Meta:
		db_table = 'orders'

	def __unicode__(self):
		return "PNR: " + unicode(self.pnr)

class Review(models.Model):

	cust = models.ForeignKey(Customer, blank = True, null = True, db_column = 'cust_id', on_delete = models.CASCADE)
	shop = models.ForeignKey(Shop, blank = True, null = True, db_column = 'shop_id', on_delete = models.CASCADE)
	msg = models.CharField("Message", max_length = 1000, blank = True, null = True)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)

	class Meta:
		db_table = 'review'

	def __unicode__(self):
		return unicode("Shop : " + self.shop.shop_name)

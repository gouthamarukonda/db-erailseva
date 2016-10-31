from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Customer(models.Model):

	cust_id = models.CharField("Customer Id", max_length = 10, primary_key = True)
	cust_name = models.CharField("Customer Name", max_length = 30, null = True, blank = True)
	email = models.CharField("Customer email", max_length = 50, null = True, blank = True)
	mobile = models.IntegerField("Mobile Number", null = True, blank = True)
	wallet_amount = models.IntegerField("Wallet Amount", null = True, blank = True)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)
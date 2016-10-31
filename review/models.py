from __future__ import unicode_literals

from django.db import models
from customer.models import Customer
from shop.models import Shop

# Create your models here.

class Review(models.Model):

	cust_id = models.ForeignKey(Customer, blank = True, null = True, on_delete = models.CASCADE)
	shop_id = models.ForeignKey(Shop, blank = True, null = True, on_delete = models.CASCADE)
	msg = models.CharField("Message", max_length = 1000, blank = True, null = True)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)
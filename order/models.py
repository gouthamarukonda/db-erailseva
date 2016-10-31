from __future__ import unicode_literals

from django.db import models
from customer.models import Customer
from pnr.models import Pnr
from fooditem.models import Fooditem
from shop.models import Shop

# Create your models here.


class Order(models.Model):

	STATUS_PENDING = '0'
	STATUS_RECEIVED = '1'
	STATUS_PREPARED = '2'
	STATUS_DISPATCHED = '3'
	STATUS_DELIVERED = '4'
	STATUS_CANCELLED = '8'
	STATUS_NOT_RECEIVED = '9'

	STATUS_CHOICES = (
	(STATUS_PENDING, 'Pending'),
	(STATUS_RECEIVED, 'Received'),
	(STATUS_PREPARED, 'Prepared'),
	(STATUS_DISPATCHED, 'Dispatched'),
	(STATUS_DELIVERED, 'Delivered'),
	(STATUS_CANCELLED, 'Cancelled'),
	(STATUS_NOT_RECEIVED, 'Not-Recieved'),
	)

	pnr_no = models.ForeignKey(Pnr, blank = True, null = True, on_delete = models.CASCADE)
	cust_id = models.ForeignKey(Customer, blank = True, null = True, on_delete = models.CASCADE)
	shop_id = models.ForeignKey(Shop, blank = True, null = True, on_delete = models.CASCADE)
	item_id = models.ForeignKey(Fooditem, blank = True, null = True, on_delete = models.CASCADE)
	status = models.CharField("Status of Order", choices = STATUS_CHOICES, max_length = 1, blank = True, null = True)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)

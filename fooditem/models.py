from __future__ import unicode_literals

from django.db import models

from shop.models import Shop

# Create your models here.

class Fooditem(models.Model):

	item_id = models.CharField("Item ID", max_length = 4, primary_key = True)
	item_name = models.CharField("Station Name", max_length = 60, null = True, blank = True)
	shop_id = models.ForeignKey(Shop, blank = True, null = True, on_delete = models.CASCADE)
	cost_per_plate = models.IntegerField("Cost per Plate", blank = True, null = True)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)
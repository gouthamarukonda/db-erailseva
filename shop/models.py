from __future__ import unicode_literals
from django.db import models
from station.models import Station

# Create your models here.

class Shop(models.Model):

	shop_id = models.CharField("Shop id", max_length = 7, primary_key = True)
	shop_name = models.CharField("Shop Name",max_length = 60, blank = True, null = True)
	station = models.ForeignKey(Station, blank = True, null = True, on_delete = models.CASCADE)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)

	class Meta:
		db_table = 'shop'

	def __unicode__(self):
		return unicode(self.shop_name)

class Fooditem(models.Model):

	item_id = models.CharField("Item ID", max_length = 4, primary_key = True)
	item_name = models.CharField("Station Name", max_length = 60, null = True, blank = True)
	shop = models.ForeignKey(Shop, blank = True, null = True, on_delete = models.CASCADE)
	cost_per_plate = models.IntegerField("Cost per Plate", blank = True, null = True)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)

	class Meta:
		db_table = 'fooditem'

	def __unicode__(self):
		return unicode(self.item_name)

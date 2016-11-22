from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

from station.models import Station
# Create your models here.

class Shop(models.Model):

	user = models.OneToOneField(User, db_column = 'user_id', on_delete = models.CASCADE)
	shop_id = models.CharField("Shop ID", db_column = 'shop_id', primary_key = True, max_length = 7)
	shop_name = models.CharField("Shop Name", max_length = 60, blank = True, null = True)
	station = models.ForeignKey(Station, blank = True, null = True, db_column = 'station_id', on_delete = models.CASCADE)
	rating = models.PositiveSmallIntegerField("Rating", blank = True, null = True, default = 0)
	numratings = models.IntegerField("Number of Ratings", blank = True, null = True, default = 0)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)

	class Meta:
		db_table = 'shop'

	def __unicode__(self):
		return unicode(self.shop_name)

class Fooditem(models.Model):

	item_id = models.CharField("Item ID", max_length = 5, primary_key = True)
	item_name = models.CharField("Station Name", max_length = 60, null = True, blank = True)
	shop = models.ForeignKey(Shop, blank = True, null = True, db_column = 'shop_id', on_delete = models.CASCADE)
	cost_per_plate = models.IntegerField("Cost per Plate", blank = True, null = True)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)

	class Meta:
		db_table = 'fooditem'

	def __unicode__(self):
		return unicode(self.item_name)

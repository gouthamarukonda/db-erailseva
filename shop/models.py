from __future__ import unicode_literals
from django.db import models
from station.models import Station

# Create your models here.

class Shop(models.Model):

	shop_id = models.CharField("Shop id", max_length = 7, primary_key = True)
	shop_name = models.CharField("Shop Name",max_length = 60, blank = True, null = True)
	station_id = models.ForeignKey(Station, blank = True, null = True, on_delete = models.CASCADE)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)
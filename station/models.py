from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Station(models.Model):

	station_id = models.CharField("Station ID", max_length = 5, primary_key = True)
	station_name = models.CharField("Station Name", max_length = 50, null = True, blank = True)
	no_of_platforms = models.IntegerField("No of Platforms", blank = True, null = True)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)

	class Meta:
		db_table = 'station'

	def __unicode__(self):
		return unicode(self.station_name)

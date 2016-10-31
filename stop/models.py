from __future__ import unicode_literals

from django.db import models
from station.models import Station
from train.models import Train

# Create your models here.

class Stop(models.Model):

	train_no = models.ForeignKey(Train, blank = True, null = True, on_delete = models.CASCADE)
	station_id = models.ForeignKey(Station, blank = True, null = True, on_delete = models.CASCADE)
	arr_time = models.TimeField("Arrival Time", null = True, blank = True)
	dept_time = models.TimeField("Departure Time", null = True, blank = True)
	stop_num = models.IntegerField("Stop Number", null = True, blank = True)
	day_of_journey = models.IntegerField("Day of Journey", blank = True, null = True)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)
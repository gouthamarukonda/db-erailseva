from django.db import models

from datetime import datetime
from station.models import Station

# Create your models here.

class Train(models.Model):

	train_no = models.CharField("Train No", max_length = 5, primary_key = True)
	train_name = models.CharField("Train Name",max_length = 50, blank = True, null = True)
	from_station_id = models.ForeignKey(Station, related_name = "start_station_train", blank = True, null = True)
	to_station_id = models.ForeignKey(Station, related_name = "end_station_train", blank = True, null = True)
	start_time = models.TimeField("Start Time", null = True, blank = True)
	end_time = models.TimeField("End Time", null = True, blank = True)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)

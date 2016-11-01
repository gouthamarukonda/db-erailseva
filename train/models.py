from django.db import models

from station.models import Station

# Create your models here.

class Train(models.Model):

	train_no = models.CharField("Train No", max_length = 5, primary_key = True)
	train_name = models.CharField("Train Name",max_length = 50, blank = True, null = True)
	from_station_id = models.ForeignKey(Station, related_name = "start_station_train", blank = True, null = True, on_delete = models.CASCADE)
	to_station_id = models.ForeignKey(Station, related_name = "end_station_train", blank = True, null = True, on_delete = models.CASCADE)
	start_time = models.TimeField("Start Time", null = True, blank = True)
	end_time = models.TimeField("End Time", null = True, blank = True)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)

	class Meta:
		db_table = 'trains'

class Stop(models.Model):

	train_no = models.ForeignKey(Train, blank = True, null = True, on_delete = models.CASCADE)
	station_id = models.ForeignKey(Station, blank = True, null = True, on_delete = models.CASCADE)
	arr_time = models.TimeField("Arrival Time", null = True, blank = True)
	dept_time = models.TimeField("Departure Time", null = True, blank = True)
	stop_num = models.IntegerField("Stop Number", null = True, blank = True)
	day_of_journey = models.IntegerField("Day of Journey", blank = True, null = True)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)

	class Meta:
		db_table = 'stops'

class Pnr(models.Model):

	pnr_no = models.CharField("Pnr No", max_length = 9, primary_key = True)
	coach_no = models.IntegerField("Coach Number", null = True, blank = True)
	berth_no = models.IntegerField("Berth Number", null = True, blank = True)
	train_start_date = models.DateTimeField("Start Date", null = True, blank = True)
	created_at = models.DateTimeField("PNR Created at", auto_now_add = True, null = True, blank = True)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)

	class Meta:
		db_table = 'pnr'

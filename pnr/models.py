from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Pnr(models.Model):

	pnr_no = models.CharField("Pnr No", max_length = 9, primary_key = True)
	coach_no = models.IntegerField("Coach Number", null = True, blank = True)
	berth_no = models.IntegerField("Berth Number", null = True, blank = True)
	train_start_date = models.DateTimeField("Start Date", null = True, blank = True)
	created_at = models.DateTimeField("PNR Created at", auto_now_add = True, null = True, blank = True)
	time_stamp = models.DateTimeField(auto_now = True, blank = True, null = True)

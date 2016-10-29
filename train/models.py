from django.db import models

# Create your models here.

class TrainModel(models.Model):

	train_no = models.CharField("Train No.", max_length = 5, primary_key = True)

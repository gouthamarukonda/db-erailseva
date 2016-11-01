from django.contrib import admin

# Register your models here.

from .models import Train, Stop, Pnr

class TrainAdmin(admin.ModelAdmin):
	list_display = ('train_no', 'train_name', 'from_station_id', 'to_station_id', 'start_time', 'end_time')

admin.site.register(Train, TrainAdmin)
admin.site.register(Stop)
admin.site.register(Pnr)

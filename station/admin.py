from django.contrib import admin

# Register your models here.

from .models import Station	

class StationAdmin(admin.ModelAdmin):
	list_display = ('station_id', 'station_name', 'no_of_platforms')

admin.site.register(Station, StationAdmin)

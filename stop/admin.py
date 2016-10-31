from django.contrib import admin

# Register your models here.
from .models import Stop	

class StopAdmin(admin.ModelAdmin):
	pass

admin.site.register(Stop, StopAdmin)
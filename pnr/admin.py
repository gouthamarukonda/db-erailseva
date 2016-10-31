from django.contrib import admin

# Register your models here.
from .models import Pnr	

class PnrAdmin(admin.ModelAdmin):
	pass

admin.site.register(Pnr, PnrAdmin)

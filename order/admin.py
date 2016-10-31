from django.contrib import admin

# Register your models here.

from .models import Order	

class OrderAdmin(admin.ModelAdmin):
	pass

admin.site.register(Order, OrderAdmin)

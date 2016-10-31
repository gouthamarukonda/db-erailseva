from django.contrib import admin

# Register your models here.

from .models import Shop

class ShopAdmin(admin.ModelAdmin):
	list_display = ('shop_id', 'shop_name', 'station_id')

admin.site.register(Shop, ShopAdmin)
from django.contrib import admin

# Register your models here.

from .models import Shop, Fooditem


class ShopAdmin(admin.ModelAdmin):
	list_display = ('shop_id', 'shop_name', 'station_id')

class FooditemAdmin(admin.ModelAdmin):
	list_display = ('item_id', 'item_name', 'shop_id','cost_per_plate')

admin.site.register(Shop, ShopAdmin)
admin.site.register(Fooditem, FooditemAdmin)
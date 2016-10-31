from django.contrib import admin
from .models import Fooditem
# Register your models here.

class FooditemAdmin(admin.ModelAdmin):
	list_display = ('item_id', 'item_name', 'shop_id','cost_per_plate')

admin.site.register(Fooditem, FooditemAdmin)
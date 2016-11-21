import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "erailseva.settings.localsettings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from datetime import datetime
from dbHandler import pgExecUpdate
from django.contrib.auth.models import User
from customer.models import Customer
from shop.models import Shop
from station.models import Station

# Create superuser

superuser = User(username = "admin")
superuser.set_password("admin12345")
superuser.is_superuser = True
superuser.is_staff = True
superuser.is_active = True
superuser.save()

# Create users for customers, shops

sample_cust_user_ids = ['10001', '10002']

for cid in sample_cust_user_ids:
	user = User(username = cid)
	user.set_password(cid)
	user.first_name = "TESTCUSTOMER" + cid[4]
	user.save()
	customer = Customer(user = user, wallet_amount = 0, mobile = "0000000000")
	customer.time_stamp = datetime.now()
	customer.save()

# Stations

for line in open('popdata/popdata0.sql'):
	if len(line) > 25:
		pgExecUpdate(line)

sample_shop_data = [
	['00001', 'KFC', '00001'],
	['00002', 'Dominos Pizza', '00001'],
	['00003', 'Subway', '00001'],
	['00004', 'McDonalds', '00002'],
	['00005', 'Pizza Hut', '00002'],
	['00006', 'Box8', '00002'],
	['00007', 'StarBucks', '00002'],
	['00008', 'Spot Burgers', '00003'],
	['00009', 'Pizza Hut', '00003'],
	['00010', 'Dominos Pizza', '00003'],
	['00011', 'Cafe Coffee Day', '00003'],
	['00012', 'Papa John''s Pizza', '00003'],
	['00013', 'Burger King', '00003'],
	['00014', 'KFC', '00004'],
	['00015', 'Dunkin Donuts', '00004'],
	['00016', 'Papa John''s Pizza', '00004'],
	['00017', 'Subway', '00004'],
	['00018', 'StarBucks', '00004'],
	['00019', 'Box8', '00005'],
	['00020', 'Papa John''s Pizza', '00005'],
	['00021', 'Cafe Coffee Day', '00005'],
	['00022', 'Burger King', '00005'],
	['00023', 'McDonalds', '00006'],
	['00024', 'Spot Burgers', '00006'],
	['00025', 'Dunkin Donuts', '00006'],
	['00026', 'Box8', '00006'],
	['00027', 'StarBucks', '00006'],
	['00028', 'Subway', '00006'],
	['00029', 'KFC', '00007'],
	['00030', 'Pizza Hut', '00007'],
	['00031', 'Dominos Pizza', '00007'],
	['00032', 'Cafe Coffee Day', '00007'],
	['00033', 'Burger King', '00007'],
	['00034', 'McDonalds', '00008'],
	['00035', 'Spot Burgers', '00008'],
	['00036', 'Dunkin Donuts', '00008'],
]

# Shops

for sdata in sample_shop_data:
	user = User(username = sdata[0])
	user.set_password(sdata[0])
	user.first_name = sdata[1] + "  " + sdata[0]
	user.save()
	station = Station.objects.get(station_id = sdata[2])
	shop = Shop(user = user, shop_id = sdata[0], shop_name = sdata[1], station = station)
	shop.rating = 0
	shop.time_stamp = datetime.now()
	shop.save()

# Fooditems

for line in open('popdata/popdata1.sql'):
	if len(line) > 25:
		pgExecUpdate(line)

# Trains, Stops, PNR

for line in open('popdata/popdata2.sql'):
	if len(line) > 25:
		pgExecUpdate(line)

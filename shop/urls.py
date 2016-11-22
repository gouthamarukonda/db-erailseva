from django.conf.urls import url
from . import views, views2

urlpatterns = [
	url(r'^getshops/$', views.get_shops_at_station),
	url(r'^getitems/$', views.get_items_at_shop),
]

urlpatterns += [
	url(r'^register/$', views2.shop_register),
	url(r'^getallstations/$', views2.get_all_stations),
	url(r'^login/$', views2.user_login),	
	url(r'^home/$', views2.orders_page),
	url(r'^fetchorders/$', views2.get_all_orders),
	url(r'^reviews/$', views2.get_reviews),
]
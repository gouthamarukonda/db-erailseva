from django.conf.urls import url
from . import views, views2

urlpatterns = [
	url(r'^getshops/$', views.get_shops_at_station),
	url(r'^getitems/$', views.get_items_at_shop),
	url(r'^login/$', views2.user_login),	
	url(r'^home/$', views2.orders_page),
	url(r'^register/$', views2.register),

]
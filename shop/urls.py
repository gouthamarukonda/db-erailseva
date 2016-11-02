from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^getshops/$', views.get_shops_at_station),
	url(r'^getitems/$', views.get_items_at_shop),
]
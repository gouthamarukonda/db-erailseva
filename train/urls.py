from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^checkpnr/$', views.checkpnr),
	url(r'^getstations/$', views.get_stations_for_pnr),
]
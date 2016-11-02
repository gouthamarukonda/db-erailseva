from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^register/$', views.register),
	url(r'^login/$', views.user_login),
	url(r'^getwalletamount/$', views.get_wallet_amount),
	url(r'^setwalletamount/$', views.set_wallet_amount),
]
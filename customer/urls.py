from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^register/$', views.register),
	url(r'^login/$', views.user_login),
	url(r'^getwalletamount/$', views.get_wallet_amount),
	url(r'^setwalletamount/$', views.set_wallet_amount),
	url(r'^placeorder/$', views.place_order),
	url(r'^getorderstatus/$', views.get_order_status),
	url(r'^cancelorder/$', views.cancel_order),
	url(r'^getprevorders/$', views.get_prev_orders),
	url(r'^postreview/$', views.post_review),

]
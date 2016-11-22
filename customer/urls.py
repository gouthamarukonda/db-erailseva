from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^register/$', views.register),
	url(r'^login/$', views.user_login),
	url(r'^home/$', views.user_home)
	url(r'^logout/$', views.user_logout),
	url(r'^getwalletamount/$', views.get_wallet_amount),
	url(r'^addwalletamount/$', views.add_wallet_amount),
	url(r'^placeorder/$', views.place_order),
	url(r'^getorderstatus/$', views.get_order_status),
	url(r'^cancelorder/$', views.cancel_order),
	url(r'^allorders/$', views.get_all_orders),
	url(r'^postreview/$', views.post_review),
]
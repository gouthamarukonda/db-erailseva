import json
import traceback

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from datetime import datetime, timedelta

from customer.models import *
from shop.models import *
from station.models import *
from dbHandler import *

@csrf_exempt
def shop_register(request):
	
	if request.method == 'POST':
		username = request.POST.get("username")
		if username == '' :
			return JsonResponse({"status": False, "msg": "Username shouldn't be empty"}) 
		shop_name = request.POST.get("shop_name")
		if shop_name == '' :
			return JsonResponse({"status": False, "msg": "Shop Name can't be empty"})
		if request.POST.get("password") == '' :
			return JsonResponse({"status": False, "msg": "password cannot be empty"})
		if request.POST.get("password_again") == '' :
			return JsonResponse({"status": False, "msg": "Retype password can't be empty"})
		if request.POST.get("password") != request.POST.get("password_again") : 
			return JsonResponse({"status": False, "msg": "Password and retype password must be same"})
		user = None
		station = None
		try:
			user = User(username = username)
			user.set_password(request.POST.get("password"))
			user.first_name = shop_name
			user.save()
		except:
			return JsonResponse({"status": False, "msg": "Given Username already in use"})
		try:
			station = Station.objects.get(station_id = request.POST.get("station_id"))
		except:
			user.delete()
			return JsonResponse({"status": False, "msg": "Given Station Doesnt Exist"})
		try:
			shop = Shop(user = user, shop_id = username, station = station, shop_name = shop_name)
			shop.rating = 0
			shop.numratings = 0
			shop.time_stamp = datetime.now()
			shop.save()
			return JsonResponse({"status": True, "msg": "Registered Successfully. Click <a href='/shop/login/'> here </a> to login"})
		except Exception as e:
			user.delete()
			return JsonResponse({"status": False, "msg": e.message})

	if request.method == 'GET':
		return render(request, 'shop/register.html')

def get_all_stations(request):
	
	if request.method == 'GET':
		try:
			qry = "select station_id, station_name from station order by station_name"
			resultset = pgExecQuery(qry)
			resp = {"status": True}
			resp["stations"] = []
			for res in resultset:
				resp["stations"].append({"id": res.station_id, "name": res.station_name})
			return JsonResponse(resp)
		except:
			return JsonResponse({"status": False})

@csrf_exempt
def user_login(request):

	if request.method == 'POST':
		try:
			user = authenticate(username = request.POST.get("username"), password = request.POST.get("password"))
			if user:
				login(request, user)
				return JsonResponse({"status": '1'})
			return JsonResponse({"status": '2'})
		except:
			return JsonResponse({"status": '3'})

	if request.method == 'GET':
		return render(request, 'shop/login.html')

@csrf_exempt
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/shop/login/')

@csrf_exempt
def orders_page(request):
	if request.method == 'GET':
		return render(request, 'shop/home.html')

@csrf_exempt
def get_all_orders(request):

	try:
		resp = {"status": True}
		resp["ongoing_orders"] = []
		resp["completed_orders"] = []
		orders = Order.objects.select_related('shop', 'shop__station', 'item').filter(shop = request.user.shop).order_by('-time_stamp')
		
		resp["this_shop_name"] = request.user.shop.shop_name
		resp["this_station_name"] = request.user.shop.station.station_name

		qry = "select day_of_journey from stop where station_id = %s"
		resultset = pgExecQuery(qry, [request.user.shop.station.station_id])


		for order in orders:
			odict={
				"order_id" : order.order_id,
				"item_name" : order.item.item_name,
				"quantity" : order.quantity,
				"del_date" : order.pnr.train_start_date + timedelta(int(resultset[0][0])),
				"train_name" : order.pnr.train.train_name,
				"coach_no" : order.pnr.coach_no,
				"berth_no" : order.pnr.berth_no,
				"payment" : order.get_paymode_display(),
				"status" : order.status,
 
			}

			if order.status in [Order.STATUS_DELIVERED, Order.STATUS_CANCELLED, Order.STATUS_CANCELLED_BY_VENDOR]:
				resp["completed_orders"].append(odict)
			else:
				resp["ongoing_orders"].append(odict)
		resp["status"] = True
		return JsonResponse(resp)
	except:
		return JsonResponse({"status": False})


@csrf_exempt
def status_change(request):
	try:
		reqdata = request.body.decode("utf-8")
		qry = "select status from orders where order_id = %s"
		resultset = pgExecQuery(qry, [request.POST.get("order_id")])
		if resultset[0].status != Order.STATUS_CANCELLED:
			qry = "update orders set status = %s where order_id = %s"
			pgExecUpdate(qry, [request.POST.get("status"), request.POST.get("order_id")])
			return JsonResponse({"status" : True , "order_id" : request.POST.get("order_id"), "statuschange" : request.POST.get("status")})
		else :
			return JsonResponse({"status" : False, "user_error" : '1' , "order_id" : request.POST.get("order_id"), "statuschange" : request.POST.get("status")})
	except:
		return JsonResponse({"status" : False})

@csrf_exempt
def get_reviews(request):

	if request.method == 'GET':
		qry = "select rating from shop where shop_id = %s"
		resultset = pgExecQuery(qry, [request.user.shop.shop_id])
		rating = resultset[0].rating
		reviews = Review.objects.filter(shop = request.user.shop).select_related('cust')
		rlist = []
		for rev in reviews:
			rlist.append({"name": rev.cust.user.first_name, "msg": rev.msg})
		return render(request, 'shop/review.html', {'rating': rating, 'reviewlist': rlist})

@csrf_exempt 
def get_menu(request):

	if request.method == 'GET':
		return render(request, 'shop/menu.html')
	else :
		pass


@csrf_exempt 
def fetch_menu(request):

	if request.method == 'GET':
		orders = Fooditem.objects.filter(shop = request.user.shop).order_by('item_name')
		rlist = []
		for rev in orders:
			rlist.append({"item_id" : rev.item_id, "item_name" : rev.item_name , "cost_per_plate" : rev.cost_per_plate})
		return JsonResponse({"rlist" : rlist, "status" :True})
	else :
		JsonResponse({"status" : False})

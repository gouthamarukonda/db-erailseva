import json
import traceback

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from datetime import datetime

from customer.models import *
from shop.models import *
from station.models import *
from dbHandler import *

@csrf_exempt
def shop_register(request):
	
	if request.method == 'POST':
		username = request.POST.get("username")
		shop_name = request.POST.get("shop_name")
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
			return JsonResponse({"status": True, "msg": "Registered Successfully"})
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
	return JsonResponse({"status": True})

@csrf_exempt
def orders_page(request):
	if request.method == 'GET':
		return render(request, 'shop/home.html')

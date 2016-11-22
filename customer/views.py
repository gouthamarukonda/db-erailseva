import json
import traceback

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Customer, Order, Review
from dbHandler import pgExecQuery, pgExecUpdate

# Create your views here.

@csrf_exempt
def createsu(request):
	if request.method == 'POST':
		try:
			reqdata = json.loads(request.body.decode("utf-8"))
			User.objects.create_superuser(reqdata['username'], '', reqdata['password'])
			return JsonResponse({"status": True})
		except:
			return JsonResponse({"status": False})

@csrf_exempt
def register(request):

	if request.method == 'POST':
		try:
			reqdata = json.loads(request.body.decode("utf-8"))
			user = User(username = reqdata["cust_id"])
			user.set_password(reqdata["password"])
			user.first_name = reqdata["cust_name"]
			user.email = reqdata["email"]
			user.save()
			customer = Customer(mobile = reqdata["mobile"])
			customer.user = user
			customer.save()
			return JsonResponse({"status": True, "msg": "Registered Successfully"})
		except:
			return JsonResponse({"status": False})

	if request.method == 'GET':
		pass

@csrf_exempt
def user_login(request):

	if request.method == 'POST':
		try:
			reqdata = json.loads(request.body.decode("utf-8"))
			user = authenticate(username = reqdata["cust_id"], password = reqdata["password"])
			if user:
				login(request, user)
				return JsonResponse({"status": True})
			return JsonResponse({"status": False, "msg": "Invalid Credentials"})
		except:
			return JsonResponse({"status": False})

	if request.method == 'GET':
		pass

@csrf_exempt
def user_home(request):
	pass

@csrf_exempt
def user_logout(request):
	logout(request)
	return JsonResponse({"status": True})

@csrf_exempt
def get_wallet_amount(request):

	try:
		qry = "select wallet_amount from customer where user_id =  %s"
		resultset = pgExecQuery(qry, [request.user.id])
		return JsonResponse({"status": True, "wallet_amount": resultset[0].wallet_amount})
	except:
		return JsonResponse({"status": False})

@csrf_exempt
def add_wallet_amount(request):

	if request.method == 'POST':
		try:
			reqdata = json.loads(request.body.decode("utf-8"))
			qry = "select wallet_amount from customer where user_id = %s"
			resultset = pgExecQuery(qry, [request.user.id])
			wallet_amount = resultset[0].wallet_amount + reqdata["amount"]
			qry = "update customer set wallet_amount = %s where user_id = %s"
			pgExecUpdate(qry, [wallet_amount, request.user.id])
			return JsonResponse({"status": True, "wallet_amount": wallet_amount})
		except:
			return JsonResponse({"status": False})

	else:
		return JsonResponse({"status": False, "msg": "Expected method = HTTP POST"})

@csrf_exempt
def place_order(request):

	if request.method == 'POST':

		reqdata = json.loads(request.body.decode("utf-8"))
		pnrno = reqdata["pnr"]
		shop_id = reqdata["shop_id"]
		paymode = reqdata["paymode"]
		cost = 0
		wallet_amount = 0
		try:
			for item in reqdata["items"]:
				qry = "select cost_per_plate from fooditem where item_id = %s"
				resultset = pgExecQuery(qry, [item["id"]])
				cost += resultset[0].cost_per_plate * item["quantity"]
			if paymode == Order.MODE_WALLET:
				qry = "select wallet_amount from customer where user_id =  %s"
				resultset = pgExecQuery(qry, [request.user.id])
				wallet_amount = resultset[0].wallet_amount
				if cost > wallet_amount:
					return JsonResponse({"status": False, "msg": "Balance in your wallet is insufficient to place the order"})
		except:
			return JsonResponse({"status": False, "msg": "Unknown Error Occured"})

		try:
			resp = {"status": True}
			resp["order_ids"] = []
			for item in reqdata["items"]:
				qry = "insert into orders(pnr_no, cust_id, shop_id, item_id, quantity, status, paymode, time_stamp) values (%s,%s,%s,%s,%s,%s,%s,now()) returning order_id"
				resultset = pgExecQuery(qry, [pnrno, request.user.id, shop_id, item["id"], item["quantity"], Order.STATUS_PENDING, paymode])
				resp["order_ids"].append(resultset[0].order_id)
			if paymode == Order.MODE_WALLET:
				qry = "update customer set wallet_amount = %s where user_id = %s"
				pgExecUpdate(qry, [wallet_amount - cost, request.user.id])
			return JsonResponse(resp)
		except:
			return JsonResponse({"status": False, "msg": "Unknown Error Occured"})

	else:
		return JsonResponse({"status": False, "msg": "Expected method = HTTP POST"})

@csrf_exempt
def get_order_status(request):

	if request.method == 'POST':
		try:
			reqdata = json.loads(request.body.decode("utf-8"))
			resp = {"status": True}
			resp["statlist"] = []
			for orderid in reqdata["order_ids"]:
				order = Order.objects.get(order_id = orderid)
				resp["statlist"].append(order.get_status_display())
			return JsonResponse(resp)
		except:
			return JsonResponse({"status": False})

	else:
		return JsonResponse({"status": False, "msg": "Expected method = HTTP POST"})

@csrf_exempt
def cancel_order(request):

	if request.method == 'POST':
		try:
			reqdata = json.loads(request.body.decode("utf-8"))
			qry = "update orders set status = %s where order_id = %s"
			pgExecUpdate(qry, [Order.STATUS_CANCELLED, reqdata["order_id"]])
			return JsonResponse({"status": True})
		except:
			return JsonResponse({"status": False})

	else:
		return JsonResponse({"status": False, "msg": "Expected method = HTTP POST"})

@csrf_exempt
def get_all_orders(request):

	try:
		resp = {"status": True}
		resp["ongoing_orders"] = []
		resp["completed_orders"] = []
		orders = Order.objects.select_related('shop', 'shop__station', 'item').filter(cust = request.user.customer).order_by('-time_stamp')
		for order in orders:
			odict = {
				"order_id": order.order_id,
				"shop_id": order.shop_id,
				"shop_name": order.shop.shop_name,
				"station_name": order.shop.station.station_name,
				"item_name": order.item.item_name,
				"quantity": order.quantity,
				"status": order.get_status_display(),
				"showrb": False,
				"showcb": False,
			}
			if order.status in [Order.STATUS_DELIVERED, Order.STATUS_CANCELLED, Order.STATUS_CANCELLED_BY_VENDOR]:
				if order.status == Order.STATUS_DELIVERED:
					odict["showrb"] = True
				resp["completed_orders"].append(odict)
			else:
				odict["showcb"] = True
				resp["ongoing_orders"].append(odict)
		return JsonResponse(resp)
	except:
		return JsonResponse({"status": False})

@csrf_exempt
def post_review(request):

	if request.method == 'POST':
		try:
			reqdata = json.loads(request.body.decode("utf-8"))
			qry = "insert into review (cust_id, shop_id, msg) values(%s, %s, %s)"
			pgExecUpdate(qry, [request.user.id, reqdata["shop_id"], reqdata["msg"]])
			posted_rating = reqdata["rating"]
			if posted_rating != 0:
				qry = "select rating, numratings from shop where shop_id=%s"
				resultset = pgExecQuery(qry, [reqdata["shop_id"]])
				_r = resultset[0].rating
				_nr = resultset[0].numratings
				new_rating = (_r * _nr + posted_rating) / (1 + _nr)
				qry = "update shop set rating = %s, numratings = %s where shop_id = %s"
				pgExecUpdate(qry, [new_rating, 1 + _nr, reqdata["shop_id"]])
			return JsonResponse({"status": True})
		except:
			return JsonResponse({"status": False})

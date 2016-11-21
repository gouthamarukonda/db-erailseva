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
		try:
			reqdata = json.loads(request.body.decode("utf-8"))
			pnrno = reqdata["pnr"]
			shop_id = reqdata["shop_id"]
			resp = {"status": True}
			resp["order_ids"] = []
			for item in reqdata["items"]:
				qry = "insert into orders(pnr_no, cust_id, shop_id, item_id, quantity, status) values(%s,%s,%s,%s,%s,%s) returning order_id"
				resultset = pgExecQuery(qry, [pnrno, request.user.id, shop_id, item["id"], item["quantity"], Order.STATUS_PENDING])
				resp["order_ids"].append(resultset[0].order_id)
			return JsonResponse(resp)
		except:
			return JsonResponse({"status": False})

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
		resp["prevorders"] = []
		orders = Order.objects.select_related('shop', 'shop__station', 'item').filter(cust = request.user.customer).order_by('-time_stamp')
		for order in orders:
			resp["prevorders"].append({
					"shop_id": order.shop_id,
					"shop_name": order.shop.shop_name,
					"station_name": order.shop.station.station_name,
					"item_name": order.item.item_name,
					"quantity": order.quantity,
					"status": order.get_status_display()
				})
		return JsonResponse(resp)
	except:
		return JsonResponse({"status": False})

@csrf_exempt
def post_review(request):

	if request.method == 'POST':
		try:
			reqdata = json.loads(request.body.decode("utf-8"))
			qry = "insert into review(cust_id, shop_id, msg) values(%s, %s, %s)"
			pgExecUpdate(qry, [request.user.id, reqdata["shop_id"], reqdata["msg"]])
			return JsonResponse({"status": True})
		except:
			return JsonResponse({"status": False})

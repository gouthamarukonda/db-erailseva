import json
import traceback

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login 
from django.contrib.auth.models import User

from .models import Customer, Order, Review
from dbHandler import *

# Create your views here.

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
			return JsonResponse({"status": True})
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
		except:
			return JsonResponse({"status": False})

	if request.method == 'GET':
		pass

@csrf_exempt
def get_wallet_amount(request):

	try:
		qry = "select wallet_amount from customer where user_id =  %(int)s)"
		resultset = pgExecQuery(qry, [request.user.id])
		return JsonResponse({"status": True, "wallet_amount": resultset[0].wallet_amount})
	except:
		return JsonResponse({"status": False})

@csrf_exempt
def set_wallet_amount(request):

	if request.method == 'POST':
		try:
			reqdata = json.loads(request.body.decode("utf-8"))
			qry = "update customer set wallet_amount = %(int)s where user_id = %(int)s)"
			pgExecUpdate(qry, [reqdata["amount"], request.user.id])
			return JsonResponse({"status": True})
		except:
			return JsonResponse({"status": False})

	else:
		return JsonResponse({"status": False, "msg": "Expected method = HTTP POST"})

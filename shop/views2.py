import json
import traceback

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

from customer.models import Customer, Order, Review
from dbHandler import pgExecQuery, pgExecUpdate

@csrf_exempt
def shop_register(request):
	pass

@csrf_exempt
def user_login(request):

	if request.method == 'POST':
		request.body.decode("utf-8")
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



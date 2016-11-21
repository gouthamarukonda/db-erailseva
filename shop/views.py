from django.shortcuts import render

# Create your views here.

import json
import traceback

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from dbHandler import *

@csrf_exempt
def get_shops_at_station(request):

	if request.method == 'POST':
		try:
			reqdata = json.loads(request.body.decode("utf-8"))
			qry = "select shop_id, shop_name from shop where station_id = %s"
			resultset = pgExecQuery(qry, [reqdata["station_id"]])
			resp = {"status": True}
			resp["shops"] = []
			for res in resultset:
				resp["shops"].append({"id": res.shop_id, "name": res.shop_name})
			return JsonResponse(resp)
		except:
			return JsonResponse({"status": False})

	else:
		return JsonResponse({"status": False, "msg": "Expected method = HTTP POST"})

@csrf_exempt
def get_items_at_shop(request):

	if request.method == 'POST':
		try:
			reqdata = json.loads(request.body.decode("utf-8"))
			qry = "select item_id, item_name, cost_per_plate from fooditem where shop_id = %s"
			resultset = pgExecQuery(qry, [reqdata["shop_id"]])
			resp = {"status": True}
			resp["items"] = []
			for res in resultset:
				resp["items"].append({"id": res.item_id, "name": res.item_name, 
					"cost": res.cost_per_plate})
			return JsonResponse(resp)
		except:
			return JsonResponse({"status": False})

	else:
		return JsonResponse({"status": False, "msg": "Expected method = HTTP POST"})
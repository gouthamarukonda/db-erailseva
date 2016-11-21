import json
import traceback

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from dbHandler import *

@csrf_exempt
def checkpnr(request):
	if request.method == 'POST':
		try:
			reqdata = json.loads(request.body.decode("utf-8"))
			qry = "select * from pnr where pnr_no = %s"
			resultset = pgExecQuery(qry, [reqdata["pnr"]])
			if len(resultset) != 0:
				return JsonResponse({"status": True})
			return JsonResponse({"status": False, "msg": "Pnr doesn't exist in database"})
		except:
			return JsonResponse({"status": False, "msg": "Exception Occured"})

@csrf_exempt
def get_stations_for_pnr(request):

	if request.method == 'POST':
		try:
			reqdata = json.loads(request.body.decode("utf-8"))
			qry = "with trainno as (select train_no as trainno from pnr where pnr_no = %s),"
			qry += "train_stops as (select station_id, stop_num from stop, trainno where train_no = trainno.trainno) "
			qry += "select station_id, station_name from train_stops natural join station order by stop_num"
			resultset = pgExecQuery(qry, [reqdata["pnr"]])
			resp = {"status": True}
			resp["stations"] = []
			for res in resultset:
				resp["stations"].append({"id": res.station_id, "name": res.station_name})
			return JsonResponse(resp)
		except Exception, e:
			return JsonResponse({"status": False, "msg": e.message})
		except:
			return JsonResponse({"status": False, "msg": "Unknown Exception Occured"})

	else:
		return JsonResponse({"status": False, "msg": "Expected method = HTTP POST"})
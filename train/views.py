import json
import traceback

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from dbHandler import *

@csrf_exempt
def get_stations_for_pnr(request):

	if request.method == 'POST':
		try:
			reqdata = json.loads(request.body.decode("utf-8"))
			qry = "with trainno as (select train_no as trainno from pnr where pnr_no = %s) "
			qry += "with train_stops as (select station_id, stop_num from stop, trainno where train_no = trainno.trainno) "
			qry += "select station_id, station_name from train_stops natural join station order by stop_num"
			resultset = pgExecQuery(qry, [reqdata["pnr"]])
			resp = {"status": True}
			resp["stations"] = []
			for res in resultset:
				resp["stations"].append({"id": res.station_id, "name": res.station_name})
			return JsonResponse(resp)
		except:
			return JsonResponse({"status": False})

	else:
		return JsonResponse({"status": False, "msg": "Expected method = HTTP POST"})
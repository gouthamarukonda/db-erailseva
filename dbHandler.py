from django.db import connection
from collections import namedtuple

def pgExec(sqlStmt, params = []):
	with connection.cursor() as cursor:
		cursor.execute(sqlStmt, params)
		rows = cursor.fetchall()
		desc = cursor.description
		rslt = namedtuple('Row', [col[0] for col in desc])
		return [rslt(*row) for row in rows]

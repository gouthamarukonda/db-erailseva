from dbHandler import pgExecUpdate

# Create customers

for line in open('popscriptdata.sql'):
	pgExecUpdate(line)

from __future__ import absolute_import
from node.celery import app
from libnmap.process import NmapProcess

@app.task
def nmap_scan(targets, options):
	
	nm = NmapProcess(targets, options)
	rc = nm.run()
	
	if nm.rc == 0:
		return nm.stdout
	else:
		return nm.stderr


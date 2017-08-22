import requests
import sys
from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
from datetime import datetime
from time import sleep

"""Script to check that prometheus server is up.  The first time it polls after 
midnight on each day, it'll reset the metric specified in METRIC.

Meant to be run within docker container
"""

PROM_HOST = 'http://localhost'
PROM_PORT = 9090
PUSH_HOST = 'http://localhost'
PUSH_PORT = 9091
METRIC = 'num_reports_ran_today'
registry = CollectorRegistry()


def check_prom_server():
    """Check that "prometheus:9090" is responding""" 
     
    # Retry loop
    for try_count in range(5):
        try:
            r = requests.get("{0}:{1}".format(PROM_HOST, PROM_PORT))
            if r.status_code == requests.codes.ok:
            	return True 
        except requests.exceptions.ConnectionError:
            print "Couldn't connect to prometheus server.  Will retry {0} more time(s)".format(str(5 - try_count - 1))
	    sleep(10)
        except:
	    pass
    
    return False
            


def pushtogateway():
    g = Gauge(METRIC, 'number of reports that ran today', registry=registry)
    g.set(0)

    # Push new metric to host "pushgateway" (listening on 9091)
    push_url = '{0}:{1}'.format(PUSH_HOST, PUSH_PORT)
    push_to_gateway(push_url, job='fife_reports_tracker', registry=registry)
    return


def main():
    while True:
        if not check_prom_server():
            print "Error connecting to prometheus client.  Is the service up?"
            sys.exit(1)

        nowdate = datetime.now() 
        try:
            if nowdate.day != lastcheck.day:
                print "{0}: Resetting pushgateway".format(nowdate)
                pushtogateway()
        except NameError:	
                pass 		# If lastcheck is not defined, do nothing

        if nowdate.minute == 0:	# Print to stdout to let us know you're still alive
                print "{0}: Hourly ping.  This is running.".format(nowdate)

        lastcheck = nowdate
        sleep(60)


if __name__ == '__main__':
    main()
    sys.exit(0)

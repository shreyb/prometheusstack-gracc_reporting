from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import time

registry = CollectorRegistry()
g = Gauge('num_reports_ran_today', 'number of reports that ran today', registry=registry)
while True:
    g.inc()
    push_to_gateway('localhost:9091', job='py_push_test', registry=registry)
    time.sleep(5) 

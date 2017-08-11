import time
import prometheus_client as pc
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = pc.Summary('request_processing_seconds', 'Time spent processing request')
g = pc.Gauge('running_reports', 'Running reports')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

def values():
   print "hello!" 

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    pc.start_http_server(8765)
    # Generate some requests.
    c = pc.Counter('test_runs', 'number of test runs')
#    while True:
#        # process_request(random.random())
##        c = pc.Counter('test_runs', "Number of test runs")
    c.inc(1)
    time.sleep(5)
    with g.track_inprogress(): 
        values()
        time.sleep(20)
    
    time.sleep(5)
         
        
